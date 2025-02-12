# Create your models here.
from django.db import models


class ChatHistory(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message[:50]
