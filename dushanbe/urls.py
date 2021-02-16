from django.urls import path
from rest_framework import routers
from dushanbe.views.bill_views import BillViewSet
from dushanbe.views.type_views import TypeViewSet
from dushanbe.views.materials_views import MaterialViewSet
from dushanbe.views.work_submission_views import WorkSubmissionViewSet
from dushanbe.views.sharepoint.share_point_views import SharePointView


# ModelViewSet router
dushanbe_router = routers.DefaultRouter()


""" Bill Routers """
# Create (POST): http://127.0.0.1:8000/api/bills/
# List (GET): http://127.0.0.1:8000/api/bills/
# Retrieve (GET): http://127.0.0.1:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
# Filter (GET): http://127.0.0.1:8000/api/bills/?id=1
dushanbe_router.register('bills', BillViewSet)


""" Type Routers """
# Create (POST): http://127.0.0.1:8000/api/types/
# List (GET): http://127.0.0.1:8000/api/types/
# Retrieve (GET): http://127.0.0.1:8000/api/types/{id}/
# Update (PUT): http://127.0.0.1:8000/api/types/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/types/{id}/
# Filter (GET): http://127.0.0.1:8000/api/types/?id=1&bill=1
dushanbe_router.register('types', TypeViewSet)


""" Material Routers """
# Create (POST): http://127.0.0.1:8000/api/materials/
# List (GET): http://127.0.0.1:8000/api/materials/
# Retrieve (GET): http://127.0.0.1:8000/api/materials/{id}/
# Update (PUT): http://127.0.0.1:8000/api/materials/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/materials/{id}/
# Filter (GET): http://127.0.0.1:8000/api/materials/?id=1&type=1&serial_no=42&unit=nr&quantity=63.00
dushanbe_router.register('materials', MaterialViewSet)


""" WorkSubmission Routers """
# Create (POST): http://127.0.0.1:8000/api/work-submissions/
# List (GET): http://127.0.0.1:8000/api/work-submissions/
# Delete (DELETE): http://127.0.0.1:8000/api/work-submissions/{id}/
# Retrieve (GET): http://127.0.0.1:8000/api/work-submissions/{id}/
# Update (PUT): http://127.0.0.1:8000/api/work-submissions/{id}/
# Filter (GET):
# http://127.0.0.1:8000/api/work-submissions/?
# id=2&bill=2&type=2&material=2&serial_no=97&unit=kits&quantity=3.69&submission_date=1998-09-22&work_progress=79&created_by=3
dushanbe_router.register('work-submissions', WorkSubmissionViewSet)


# APIView
urlpatterns = [

    # -------------------- SharePoint Testing --------------------

    # http://127.0.0.1:8000/api/sharepoint/
    path('sharepoint/', SharePointView.as_view())

]

