from django.urls import path

from apps.users.views.user_views import *

urlpatterns = [
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/register/', RegisterUserGenericView.as_view(), name='user-register'),
    path('users/login/', LoginUserView.as_view(), name='user-login'),
    path('users/logout/', LogoutUserView.as_view(), name='user-logout'),
]
