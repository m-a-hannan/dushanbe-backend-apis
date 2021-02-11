from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# app
from dushanbe.models import WorkSubmission
# from dushanbe.filters.filters import WorkSubmissionFilter
from dushanbe.paginations.paginations import CustomPageNumberPagination
from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
from dushanbe.serializers.work_submission_serializers import (
    WorkSubmissionCreateSerializer,
    WorkSubmissionUpdateSerializer,
    WorkSubmissionListSerializer
)


# Create (POST): http://127.0.0.1:8000/api/work-submissions/
# List (GET): http://127.0.0.1:8000/api/work-submissions/
# Delete (DELETE): http://127.0.0.1:8000/api/work-submissions/{id}/
# Retrieve (GET): http://127.0.0.1:8000/api/work-submissions/{id}/
# Update (PUT): http://127.0.0.1:8000/api/work-submissions/{id}/
# Filter (GET): http://127.0.0.1:8000/api/work-submissions/?bill=1&type=1&serial_no=2&unit=kits&quantity=1.00&submission_date=2021-02-07&work_progress=2&created_by=1
class WorkSubmissionViewSet(viewsets.ModelViewSet):
    queryset = WorkSubmission.objects.all().order_by('-id')
    serializer_class = WorkSubmissionListSerializer
    # permission_classes = (DjangoModelPermissionsWithGET, )
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = WorkSubmissionFilter
    pagination_class = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = WorkSubmissionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = WorkSubmissionUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


