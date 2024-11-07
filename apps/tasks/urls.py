from django.urls import path

from apps.tasks.views.tag_views import *
from apps.tasks.views.task_views import *

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags'),
    path('tags/<int:pk>/', TagApi.as_view(), name='tags'),
    path('tasks/', TasksListAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='tasks'),
]
