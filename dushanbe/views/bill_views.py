from django.db import transaction
from django.db.models import Count, Q
from rest_framework import status, viewsets
from rest_framework.response import Response

# app
from dushanbe.models import Bill
from dushanbe.paginations.paginations import CustomPageNumberPagination
from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
from dushanbe.serializers.bill_serializers import (
    BillCreateSerializer,
    BillUpdateSerializer,
    BillListSerializer
)


# Create (POST): http://0.0.0.0:8000/api/bills/
# List (GET): http://0.0.0.0:8000/api/bills/
# Retrieve (GET): http://0.0.0.0:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all().order_by('bill_name')
    serializer_class = BillListSerializer
    permission_classes = (DjangoModelPermissionsWithGET, )
    pagination_class = CustomPageNumberPagination

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


