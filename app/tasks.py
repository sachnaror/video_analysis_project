import json
import os
import time

import cv2
import nltk
import pytesseract
import whisper
from celery import shared_task
from django.db import transaction
from moviepy.editor import VideoFileClip
from transformers import pipeline
from ultralytics import YOLO

from .models import VideoAnalysis

# ✅ Download necessary NLP models
nltk.download('punkt')

# ✅ Define Paths
MEDIA_DIR = "media"
UPLOADS_DIR = os.path.join(MEDIA_DIR, "uploads")
FRAMES_DIR = os.path.join(MEDIA_DIR, "frames")
TRANSCRIPTS_DIR = os.path.join(MEDIA_DIR, "transcripts")
ANALYSIS_DIR = os.path.join(MEDIA_DIR, "analysis")

for folder in [UPLOADS_DIR, FRAMES_DIR, TRANSCRIPTS_DIR, ANALYSIS_DIR]:
    os.makedirs(folder, exist_ok=True)

# ✅ Load Whisper Model (Speech-to-Text)
whisper_model = whisper.load_model("base")

# ✅ Load YOLOv8 Model (Object Detection)
yolo_model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model (lightweight)

# ✅ Update Progress Utility
def update_progress(progress, stage, report_ready=False):
    """Write progress status to JSON file"""
    progress_file = os.path.join(MEDIA_DIR, "progress.json")
    with open(progress_file, "w") as f:
        json.dump({"progress": progress, "stage": stage, "report_ready": report_ready}, f)

@shared_task
def process_video_task(video_filename):
    """Process Video with ML Models"""
    video_path = os.path.join(UPLOADS_DIR, video_filename)

    update_progress(10, "Extracting frames from video...")

    # ✅ Step 1: Extract Frames from Video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(FRAMES_DIR, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()

    # ✅ Step 2: Extract Audio & Convert to Text using Whisper
    update_progress(30, "Extracting speech & transcribing...")
    transcript_text = "No speech detected."

    try:
        audio_path = video_path.replace(".mp4", ".wav")
        clip = VideoFileClip(video_path)

        if clip.audio:  # ✅ Check if video contains audio before extracting
            clip.audio.write_audiofile(audio_path)
            transcript_text = whisper_model.transcribe(audio_path)["text"]

    except Exception as e:
        print(f"Audio extraction error: {str(e)}")

    transcript_path = os.path.join(TRANSCRIPTS_DIR, f"{video_filename}_transcript.txt")
    with open(transcript_path, "w") as f:
        f.write(transcript_text)

    # ✅ Step 3: Apply OCR to Extract Text from Frames
    update_progress(50, "Running OCR on frames...")
    ocr_text = ""

    def preprocess_image(img_path):
        """Pre-process image for better OCR results"""
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return thresh  # ✅ Return processed image

    for img_file in os.listdir(FRAMES_DIR):
        img_path = os.path.join(FRAMES_DIR, img_file)
        processed_img = preprocess_image(img_path)  # ✅ Preprocess before OCR
        text = pytesseract.image_to_string(processed_img)
        ocr_text += text.strip() + "\n"

    # ✅ Step 4: Perform Object Detection using YOLO
    update_progress(70, "Detecting objects in frames...")
    detected_objects = []

    for img_file in os.listdir(FRAMES_DIR):
        img_path = os.path.join(FRAMES_DIR, img_file)

        try:
            results = yolo_model(img_path)
            detected_objects.extend([r.names[int(c)] for r in results for c in r.boxes.cls])

        except Exception as e:
            print(f"YOLO Detection Error on {img_file}: {str(e)}")

    detected_objects = list(set(detected_objects))  # ✅ Remove duplicates

    # ✅ Step 5: Apply NLP for Video Analysis
    update_progress(90, "Running NLP-based analysis...")
    summary = "No summary available."

    try:
        nlp_pipeline = pipeline("summarization")
        summary = nlp_pipeline(transcript_text[:1000], max_length=150, min_length=50, do_sample=False)[0]["summary_text"]

    except Exception as e:
        print(f"NLP Summarization Error: {str(e)}")

    # ✅ Step 6: Save Processed Data
    analysis_text = f"Summary: {summary}\n\nExtracted Text: {ocr_text}\n\nObjects Detected: {', '.join(detected_objects)}"

    analysis_path = os.path.join(ANALYSIS_DIR, f"{video_filename}_analysis.txt")
    with open(analysis_path, "w") as f:
        f.write(analysis_text)

    # ✅ Save to Database (Ensuring Atomic Transactions)
    with transaction.atomic():
        VideoAnalysis.objects.create(
            video_name=video_filename,
            transcript=transcript_text,
            analysis=analysis_text
        )

    update_progress(100, "Processing complete! Report ready.", report_ready=True)
    return "Processing Completed"
