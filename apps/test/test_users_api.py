import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.users.models import User
from apps.users.serializers.user_serializers import UserListSerializer
from unittest.mock import patch
from apps.projects.models.project import Project


@pytest.fixture
def user_fixture(db):
    project = Project.objects.create(name="project1")
    User.objects.all().delete()
    return User.objects.bulk_create([
        User(username='user1', email='user1@example.com', first_name='User', last_name='One', position='PROGRAMMER', project=project),
        User(username='user2', email='user2@example.com', first_name='User', last_name='Two', position='PROGRAMMER', project=project),
    ])


@pytest.mark.django_db
class TestUserAPI:
    @pytest.fixture(autouse=True)
    def setup(self, user_fixture):
        self.client = APIClient()
        self.client.force_authenticate(user=User.objects.first())

    def test_get_all_users(self, user_fixture):
        url = reverse('user-list')
        response = self.client.get(url)
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_get_users_by_project_name(self, user_fixture):
        url = reverse('user-list') + '?project_name=project1'
        response = self.client.get(url)
        users = User.objects.filter(project__name='project1')
        serializer = UserListSerializer(users, many=True)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    @patch('apps.users.models.User.objects.all', return_value=User.objects.none())
    def test_get_empty_user_list(self, mock_users):
        url = reverse('user-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(response.data) == 0
        mock_users.assert_called_once()

    def test_user_serializer_representation(self, user_fixture):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        for user in serializer.data:
            assert 'username' in user
            assert 'email' in user
            assert 'first_name' in user
            assert 'last_name' in user
