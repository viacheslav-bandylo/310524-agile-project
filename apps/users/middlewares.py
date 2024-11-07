from datetime import datetime

from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class JWTAuthMiddleware(MiddlewareMixin):
    def refresh_access_token(self, request):
        try:
            refresh = RefreshToken(request)
            new_access_token = str(refresh.access_token)
            return new_access_token
        except TokenError:
            return None

    def clear_cookies(self, request):
        request.COOKIES.pop('access_token', None)
        request.COOKIES.pop('refresh_token', None)

    def process_request(self, request):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token:
            try:
                token = AccessToken(access_token)

                if datetime.utcfromtimestamp(token['exp']) < datetime.utcnow():
                    raise TokenError('Token expired')

                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
            except TokenError:
                new_access_token = self.refresh_access_token(refresh_token)

                if new_access_token:
                    request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'
                    request._new_access_token = new_access_token
                else:
                    self.clear_cookies(request)
        elif refresh_token:
            new_access_token = self.refresh_access_token(refresh_token)

            if new_access_token:
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'
                request._new_access_token = new_access_token
            else:
                self.clear_cookies(request)

    def process_response(self, request, response):
        new_access_token = getattr(request, '_new_access_token', None)

        if new_access_token:
            access_expiry = datetime.utcfromtimestamp(AccessToken(new_access_token)['exp'])
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                expires=access_expiry,
                httponly=True,
                samesite='Lax',
            )

        return response
