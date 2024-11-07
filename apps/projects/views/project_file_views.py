from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.projects.models import ProjectFile, Project
from apps.projects.serializers.project_file_serializers import (
    AllProjectFilesSerializer,
    CreateProjectFileSerializer,
)


class ProjectFileListAPIView(ListCreateAPIView):
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            serializer = AllProjectFilesSerializer
        elif self.request.method == 'POST':
            serializer = CreateProjectFileSerializer

        return serializer

    def get_queryset(self):
        project_name = self.request.query_params.get('project')

        if project_name:
            project_file = ProjectFile.objects.filter(
                project__name=project_name
            )
            return project_file

        return ProjectFile.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:
        project_files = self.get_queryset()

        if not project_files.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = self.get_serializer(project_files, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request: Request, *args, **kwargs) -> Response:
        file_content = request.FILES["file_path"]
        project_id = request.data.pop("project_id")
        request.data['file_name'] = file_content.name if file_content else None

        project = get_object_or_404(Project, pk=project_id)

        serializer = self.get_serializer(
            data=request.data,
            context={
                "raw_file": file_content,
                "project": project
            }
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                data={
                    "message": "File upload successfully"
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
