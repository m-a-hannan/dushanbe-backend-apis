from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# app
from dushanbe.models import BillSubmission
from dushanbe.filters.filters import BillSubmissionFilter
from dushanbe.paginations.paginations import CustomPageNumberPagination
from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
from dushanbe.serializers.bill_submission_serializers import (
    BillSubmissionCreateSerializer,
    BillSubmissionUpdateSerializer,
    BillSubmissionListSerializer
)


# Create (POST): http://127.0.0.1:8000/api/bill-submissions/
# List (GET): http://127.0.0.1:8000/api/bill-submissions/
# Delete (DELETE): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Retrieve (GET): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Filter (GET): http://127.0.0.1:8000/api/bill-submissions/?
# bill=1&type=1&material=2&serial_no=2&unit=kits&quantity=1.00&submission_date=2021-02-07&work_progress=2&created_by=1
class BillSubmissionViewSet(viewsets.ModelViewSet):
    queryset = BillSubmission.objects.all().order_by('-id')
    serializer_class = BillSubmissionListSerializer
    # permission_classes = (DjangoModelPermissionsWithGET, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = BillSubmissionFilter
    pagination_class = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = BillSubmissionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = BillSubmissionUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


