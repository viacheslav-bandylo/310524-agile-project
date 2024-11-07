from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers, status
from rest_framework.views import APIView

from ..models.project import Project


class AllProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at']


class CreateProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['created_at']

        def validate_description(self, value):
            if len(value) < 30:
                raise serializers.ValidationError('Description must be at least 30 characters')
            return value


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'count_of_files']


class ProjectShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')
