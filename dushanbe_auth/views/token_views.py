from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from dushanbe_auth.serializers.token_serializers import TokenListSerializer
from dushanbe_auth.permissions.common_permissions import DjangoModelPermissionsWithGET


# List (GET): http://127.0.0.1:8000/api/tokens/
class TokenReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenListSerializer
    permission_classes = (DjangoModelPermissionsWithGET,)
    pagination_class = None

    