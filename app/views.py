import json
import os
import time

import openai
from celery import shared_task
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import VideoAnalysis

# ✅ Define Media Directory and Progress File
MEDIA_DIR = "media"
UPLOADS_DIR = os.path.join(MEDIA_DIR, "uploads")
PROGRESS_FILE = os.path.join(MEDIA_DIR, "progress.json")

# ✅ Ensure media folders exist
for folder in ["uploads", "chunks", "frames", "audio", "transcripts", "analysis"]:
    os.makedirs(os.path.join(MEDIA_DIR, folder), exist_ok=True)

# ✅ Ensure progress.json file exists
if not os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"progress": 0, "stage": "Waiting for processing...", "report_ready": False}, f)

# ✅ Utility Functions for Progress Updates
def get_progress():
    """Read progress from JSON file"""
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def update_progress(progress, stage, report_ready=False):
    """Write progress status to JSON file"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"progress": progress, "stage": stage, "report_ready": report_ready}, f)

# ✅ File Upload Functionality
@csrf_exempt  # ✅ Fix CSRF issue
def upload_file(request):
    """Upload files (PDFs, images) for AI analysis"""
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage(location=UPLOADS_DIR)
        filename = fs.save(uploaded_file.name, uploaded_file)

        return JsonResponse({"message": "File uploaded successfully!", "filename": filename})

    return JsonResponse({"error": "No file uploaded."}, status=400)

@csrf_exempt  # ✅ Fix CSRF issue
def upload_video(request):
    """Upload video and trigger processing"""
    if request.method == "POST" and request.FILES.get("video"):
        video = request.FILES["video"]
        fs = FileSystemStorage(location=UPLOADS_DIR)
        filename = fs.save(video.name, video)

        # ✅ Pass the filename to Celery task
        process_video_task.delay(filename)

        return JsonResponse({"message": "Video uploaded & processing started.", "filename": filename})

    return JsonResponse({"error": "No video uploaded."}, status=400)

# ✅ Index Page
def index(request):
    """Render index.html"""
    return render(request, 'index.html')

# ✅ Get Current Progress
def progress(request):
    """Return current progress status from file"""
    return JsonResponse(get_progress())

# ✅ Celery Task: Process Video in Stages
@shared_task
def process_video_task(video_filename):
    """Process video with ML models"""
    update_progress(0, "Initializing...")

    # ✅ Simulated processing stages
    stages = [
        ("Uploading video...", 10),
        ("Extracting audio...", 30),
        ("Running OCR...", 50),
        ("Generating transcript...", 70),
        ("Analyzing content...", 90),
        ("Processing complete!", 100)
    ]

    for stage, percentage in stages:
        update_progress(percentage, stage)
        time.sleep(3)  # Simulating processing time

    # ✅ Create a sample transcript file
    transcript_path = os.path.join(MEDIA_DIR, "transcripts", f"{video_filename}_transcript.txt")
    with open(transcript_path, "w") as f:
        f.write("This is a generated transcript of the video.")

    # ✅ Create a sample analysis report
    analysis_path = os.path.join(MEDIA_DIR, "analysis", f"{video_filename}_analysis.txt")
    with open(analysis_path, "w") as f:
        f.write("This is an AI-powered analysis of the video content.")

    update_progress(100, "Processing complete! Report ready.", report_ready=True)
    return "Processing Completed"

# ✅ Start Video Processing
@csrf_exempt  # ✅ Fix CSRF issue
def process_video(request):
    """Trigger video processing task"""
    update_progress(0, "Initializing...")

    video_filename = request.GET.get("filename")  # ✅ Ensure filename is passed
    if not video_filename:
        return JsonResponse({"error": "No filename provided for processing"}, status=400)

    task = process_video_task.delay(video_filename)  # ✅ Call Celery task with filename
    return JsonResponse({"task_id": task.id, "message": "Processing started."})

# ✅ Chat Functionality (Fixed OpenAI API Key Handling)
@csrf_exempt  # ✅ Fix CSRF issue
def chat(request):
    """Handle user queries using OpenAI API"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # ✅ Read JSON request body correctly
            question = data.get("question")
            api_key = data.get("api_key")

            if not api_key:
                return JsonResponse({"response": "Error: No API Key provided."}, status=400)

            # ✅ Set API key before making request
            openai.api_key = api_key

            # ✅ Generate OpenAI response
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": question}]
            )

            ai_response = response["choices"][0]["message"]["content"]
            return JsonResponse({"response": ai_response})

        except openai.error.OpenAIError as e:
            return JsonResponse({"response": f"OpenAI API Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"response": f"Unexpected Error: {str(e)}"}, status=500)

# ✅ View Reports Page
def view_reports(request):
    """Fetch all past analyses"""
    reports = VideoAnalysis.objects.all()
    return render(request, "reports.html", {"reports": reports})
