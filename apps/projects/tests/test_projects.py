from django.db.models import QuerySet
from django.test import TestCase
from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.projects.models import Project
from apps.projects.serializers.project_serializer import AllProjectSerializer
from apps.projects.views.project_views import ProjectListAPIView


class TestProjectModel(TestCase):

    def test_project_str(self):
        # Создаем MagicMock объект
        mock_project = MagicMock(spec=Project)
        mock_project.name = 'Test Project'

        # Устанавливаем возвращаемое значение метода __str__
        mock_project.__str__.return_value = 'Test Project'

        # Проверяем, что метод __str__ возвращает ожидаемое значение
        self.assertEqual(str(mock_project), 'Test Project')


class TestProjectListAPIView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('project-list')

        # Создание фикстур проектов
        self.project1 = Project.objects.create(
            name='Project 1',
            description='Test Description for the first test project with description more than 50 chars.',
        )
        self.project2 = Project.objects.create(
            name='Project 2',
            description='Test Description for the second test project with description more than 50 chars.',
        )

    @patch.object(ProjectListAPIView, 'get_objects', return_value=Project.objects.none())
    def test_get_empty_project_list(self, mock_get_objects):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, [])

    @patch.object(ProjectListAPIView, 'get_objects')
    def test_get_project_list(self, mock_get_objects):
        projects = [self.project1, self.project2]

        mock_queryset = MagicMock(spec=QuerySet)
        mock_queryset.__iter__.return_value = iter(projects)
        mock_get_objects.return_value = mock_queryset

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка содержимого ответа
        serializer = AllProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_project(self):
        data = {
            'name': 'New Project',
            'description': 'Test Description for the first test project with description more than 50 chars.'
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка данных созданного проекта
        self.assertTrue(Project.objects.filter(name='New Project').exists())
        project = Project.objects.get(name='New Project')
        self.assertEqual(
            project.description,
            'Test Description for the first test project with description more than 50 chars.'
        )
