from django.db import models
from ..models.project_file import ProjectFile


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ManyToManyField(ProjectFile, related_name='projects')

    @property
    def count_of_files(self):
        return self.file.count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
