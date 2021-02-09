from django.urls import path
from rest_framework import routers
from dushanbe.views.bill_views import BillViewSet
from dushanbe.views.type_views import TypeViewSet
from dushanbe.views.materials_views import MaterialViewSet
from dushanbe.views.bill_submission_views import BillSubmissionViewSet


# ModelViewSet router
dushanbe_router = routers.DefaultRouter()


""" Bill Routers """
# Create (POST): http://127.0.0.1:8000/api/bills/
# List (GET): http://127.0.0.1:8000/api/bills/
# Retrieve (GET): http://127.0.0.1:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
dushanbe_router.register('bills', BillViewSet)


""" Type Routers """
# Create (POST): http://127.0.0.1:8000/api/types/
# List (GET): http://127.0.0.1:8000/api/types/
# Retrieve (GET): http://127.0.0.1:8000/api/types/{id}/
# Update (PUT): http://127.0.0.1:8000/api/types/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/types/{id}/
# Filter (GET): http://127.0.0.1:8000/api/types/?type_name=Edited&material=3&serial_no=3&unit=nr&quantity=2.00
dushanbe_router.register('types', TypeViewSet)


""" Material Routers """
# Create (POST): http://127.0.0.1:8000/api/materials/
# List (GET): http://127.0.0.1:8000/api/materials/
# Retrieve (GET): http://127.0.0.1:8000/api/materials/{id}/
# Update (PUT): http://127.0.0.1:8000/api/materials/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/materials/{id}/
dushanbe_router.register('materials', MaterialViewSet)


""" BillSubmission Routers """
# Create (POST): http://127.0.0.1:8000/api/bill-submissions/
# List (GET): http://127.0.0.1:8000/api/bill-submissions/
# Delete (DELETE): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Retrieve (GET): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Filter (GET): http://127.0.0.1:8000/api/bill-submissions/?bill=1&type=1&serial_no=2&unit=kits&quantity=1.00&submission_date=2021-02-07&work_progress=2&created_by=1
dushanbe_router.register('bill-submissions', BillSubmissionViewSet)


# APIView
urlpatterns = [

]

