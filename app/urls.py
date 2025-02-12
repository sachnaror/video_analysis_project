from django.urls import path

from . import views  # ✅ Import all views
from .views import (upload_video,  # ✅ Explicitly import required views
                    view_reports)

urlpatterns = [
    path('', views.index, name='index'),  # ✅ Ensure views.index exists
    path('process_video/', views.process_video, name='process_video'),
    path('progress/', views.progress, name='progress'),
    path("upload_video/", upload_video, name="upload_video"),
    path("reports/", view_reports, name="view_reports"),
]
