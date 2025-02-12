import time

import openai
from celery import shared_task
from django.http import JsonResponse
from django.shortcuts import render


def index(request):  # ✅ Ensure this function exists
    return render(request, 'index.html')  # ✅ Ensure 'index.html' exists in templates folder



progress_status = {
    "progress": 0,
    "stage": "Starting processing..."  # ✅ Track current stage
}

def progress(request):
    """Return current progress status"""
    return JsonResponse(progress_status)

@shared_task
def process_video_task():
    """Simulate video processing in stages"""
    global progress_status

    stages = [
        "Uploading video...",
        "Extracting audio...",
        "Running OCR...",
        "Generating transcript...",
        "Analyzing content...",
        "Processing complete!"
    ]

    for i, stage in enumerate(stages):
        progress_status["progress"] = (i + 1) * (100 // len(stages))
        progress_status["stage"] = stage
        time.sleep(3)  # Simulating processing time

    progress_status["progress"] = 100  # Ensure it reaches 100%
    return "Processing Completed"

def process_video(request):
    """Trigger Celery task for video processing"""
    global progress_status
    progress_status = {"progress": 0, "stage": "Initializing..."}  # Reset status

    task = process_video_task.delay()  # ✅ Call Celery task
    return JsonResponse({"task_id": task.id, "message": "Processing started."})

def chat(request):
    if request.method == "POST":
        data = request.POST
        question = data.get("question")
        api_key = data.get("api_key")

        if not api_key:
            return JsonResponse({"response": "Error: No API Key provided."}, status=400)

        # ✅ Generate OpenAI response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            api_key=api_key
        )

        ai_response = response["choices"][0]["message"]["content"]

        return JsonResponse({"response": ai_response})
