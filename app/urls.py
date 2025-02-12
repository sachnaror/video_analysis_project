from django.urls import path

from . import views  # ✅ Ensure this import exists

urlpatterns = [
    path('', views.index, name='index'),  # ✅ Correct reference to views.index
    path('process_video/', views.process_video, name='process_video'),
    path('progress/', views.progress, name='progress'),
]
