from rest_framework import status, viewsets
from django.contrib.auth.models import Permission
from dushanbe_auth.serializers.permission_serializers import PermissionSerializer
from dushanbe_auth.permissions.common_permissions import DjangoModelPermissionsWithGET


# List (GET): http://127.0.0.1:8000/api/permissions/
class PermissionReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (DjangoModelPermissionsWithGET,)
    pagination_class = None

