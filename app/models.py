from django.db import models


class VideoAnalysis(models.Model):
    video_name = models.CharField(max_length=255)
    transcript = models.TextField()
    analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_name
