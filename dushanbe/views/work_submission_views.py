from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# SharePoint
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# app
from dushanbe.filters.filters import WorkSubmissionFilter
from dushanbe.models import Bill, Type, Material, WorkSubmission
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
# Filter (GET):
# http://127.0.0.1:8000/api/work-submissions/?
# id=2&bill=2&type=2&material=2&serial_no=97&unit=kits&quantity=3.69&submission_date=1998-09-22&work_progress=79&created_by=3
class WorkSubmissionViewSet(viewsets.ModelViewSet):
    queryset = WorkSubmission.objects.all().order_by('-id')
    serializer_class = WorkSubmissionListSerializer
    permission_classes = (DjangoModelPermissionsWithGET, )
    # authentication_classes = []
    # permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkSubmissionFilter
    pagination_class = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = WorkSubmissionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        work_submission_obj = serializer.save()

        ## sharepoint config
        sharepoint_username = "Bangladesh.IT1@ludwigpfeiffer.com"
        sharepoint_password = "A%vhTlN90Z%M"
        sharepoint_url = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
        sharepoint_website = "https://ludwpfeiffer.sharepoint.com"
        sharepoint_authcookie = Office365(sharepoint_website, username=sharepoint_username, password=sharepoint_password).GetCookies()
        site = Site(sharepoint_url, version=Version.v2016, authcookie=sharepoint_authcookie)
        # sharepoint_list_directory = site.List('python_sync')
        sharepoint_list_directory = site.List('Dushanbe API Data (Testing)')

        sharepoint_data = [
            {
                "Bill Name": work_submission_obj.bill.bill_name,
                "Type Name": work_submission_obj.type.type_name,
                "Material Name": work_submission_obj.material.material_name,
                "Submission Date": work_submission_obj.submission_date,
                "Work Progress": work_submission_obj.work_progress,
                # "CreatedBy": work_submission_obj.created_by,
                # "Active Status": work_submission_obj.active_status
            }
        ]

        # sharepoint_obj = sharepoint_list_directory.CreateListItems(data=data, kind='New')
        sharepoint_obj = sharepoint_list_directory.UpdateListItems(data=sharepoint_data, kind='New')
        print('--sharepoint_obj--', sharepoint_obj)
        ## sharepoint config end

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # original
        # serializer = WorkSubmissionCreateSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = WorkSubmissionUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


