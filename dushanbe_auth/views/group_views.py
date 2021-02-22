from rest_framework import viewsets
from django.contrib.auth.models import Group
from dushanbe_auth.serializers.group_serializers import GroupSerializer
from dushanbe_auth.permissions.common_permissions import DjangoModelPermissionsWithGET


# List (GET): http://127.0.0.1:8000/api/groups/
class GroupReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (DjangoModelPermissionsWithGET,)
    pagination_class = None

