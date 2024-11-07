from django.urls import path, include
from .views.project_views import *
from .views.project_file_views import *

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
    path('files/', ProjectFileListAPIView.as_view()),
]