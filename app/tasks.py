import time

from celery import shared_task


@shared_task
def process_video_task():
    progress = 0
    for _ in range(10):
        progress += 10
        time.sleep(2)  # Simulate processing time
    return "Processing Completed"
