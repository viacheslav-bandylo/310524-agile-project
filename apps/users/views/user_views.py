from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.serializers.user_serializers import *


class UserListGenericView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name')

        if project_name:
            return User.objects.filter(project__name=project_name)

        return User.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:
        users = self.get_queryset()

        if not users.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = self.get_serializer(users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class RegisterUserGenericView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)

        if user:
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            access_expiry = datetime.utcfromtimestamp(access_token['exp'])
            refresh_expiry = datetime.utcfromtimestamp(refresh_token['exp'])

            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(
                key='access_token',
                value=str(access_token),
                httponly=True,
                secure=False,
                samesite='Lax',
                expires=access_expiry,
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh_token),
                httponly=True,
                secure=False,
                samesite='Lax',
                expires=refresh_expiry,
            )
            return response
        else:
            return Response({'details': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(key='access_token')
        response.delete_cookie(key='refresh_token')
        return response
