from django.urls import path, include

urlpatterns = [
    path('', include('apps.tasks.urls')),
    path('', include('apps.projects.urls')),
    path('', include('apps.users.urls')),
]
