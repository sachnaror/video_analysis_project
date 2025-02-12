from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_video/', views.process_video, name='process_video'),
    path('chat/', views.chat, name='chat'),
]
