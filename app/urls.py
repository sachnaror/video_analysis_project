from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_video/', views.process_video, name='process_video'),
    path('progress/', views.progress, name='progress'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_file/', views.upload_file, name='upload_file'),  # ✅ FIX: Add missing file upload route
    path('chat/', views.chat, name='chat'),
    path('reports/', views.view_reports, name='view_reports'),
]
