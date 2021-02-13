from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# app
from dushanbe.models import Bill
from dushanbe.filters.filters import BillFilter
from dushanbe.paginations.paginations import CustomPageNumberPagination
from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
from dushanbe.serializers.bill_serializers import (
    BillCreateSerializer,
    BillUpdateSerializer,
    BillListSerializer
)


# Create (POST): http://127.0.0.1:8000/api/bills/
# List (GET): http://127.0.0.1:8000/api/bills/
# Retrieve (GET): http://127.0.0.1:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
# Filter (GET): http://127.0.0.1:8000/api/bills/?id=1
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all().order_by('-id')
    serializer_class = BillListSerializer
    permission_classes = (DjangoModelPermissionsWithGET, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = BillFilter
    pagination_class = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = BillCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = BillUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


