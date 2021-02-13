from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# app
from dushanbe.models import Type
from dushanbe.filters.filters import TypeFilter
from dushanbe.paginations.paginations import CustomPageNumberPagination
from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
from dushanbe.serializers.type_serializers import (
    TypeCreateSerializer,
    TypeUpdateSerializer,
    TypeListSerializer
)


# Create (POST): http://127.0.0.1:8000/api/types/
# List (GET): http://127.0.0.1:8000/api/types/
# Retrieve (GET): http://127.0.0.1:8000/api/types/{id}/
# Update (PUT): http://127.0.0.1:8000/api/types/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/types/{id}/
# Filter (GET): http://127.0.0.1:8000/api/types/?id=1&bill=1
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('-id')
    serializer_class = TypeListSerializer
    permission_classes = (DjangoModelPermissionsWithGET, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = TypeFilter
    pagination_class = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = TypeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = TypeUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     return self.queryset.filter(bill=1)




