from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from dushanbe_auth.serializers.user_serializers import UserLoginResponseSerializer


# Login (POST) (No Token): http://127.0.0.1:8000/api/login/
class Login(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login_response_serializer = UserLoginResponseSerializer(user)
        user_permissions = login_response_serializer.data['user_permissions']

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "active_status": user.is_active,
                "superuser_status": user.is_superuser,
                "token": token.key,
                "user_permissions": user_permissions
            },
            status=status.HTTP_200_OK
        )


# Logout (GET): http://127.0.0.1:8000/api/logout/
class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "logout successful"}, status=status.HTTP_200_OK)

