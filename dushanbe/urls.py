from django.urls import path
from rest_framework import routers
from dushanbe.views.bill_views import BillViewSet
from dushanbe.views.type_views import TypeViewSet
from dushanbe.views.materials_views import MaterialViewSet
from dushanbe.views.bill_submission_views import BillSubmissionViewSet


# ModelViewSet router
dushanbe_router = routers.DefaultRouter()


""" Bill Routers """
# Create (POST): http://0.0.0.0:8000/api/bills/
# List (GET): http://0.0.0.0:8000/api/bills/
# Retrieve (GET): http://0.0.0.0:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
dushanbe_router.register('bills', BillViewSet)


""" Type Routers """
# Create (POST): http://0.0.0.0:8000/api/types/
# List (GET): http://0.0.0.0:8000/api/types/
# Retrieve (GET): http://0.0.0.0:8000/api/types/{id}/
# Update (PUT): http://127.0.0.1:8000/api/types/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/types/{id}/
dushanbe_router.register('types', TypeViewSet)


""" Material Routers """
# Create (POST): http://0.0.0.0:8000/api/materials/
# List (GET): http://0.0.0.0:8000/api/materials/
# Retrieve (GET): http://0.0.0.0:8000/api/materials/{id}/
# Update (PUT): http://127.0.0.1:8000/api/materials/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/materials/{id}/
dushanbe_router.register('materials', MaterialViewSet)


# """ Work Routers """
# Create (POST): http://0.0.0.0:8000/api/bill-submissions/
# List (GET): http://0.0.0.0:8000/api/bill-submissions/
# Delete (DELETE): http://127.0.0.1:8000/api/bill-submissions/{id}/
# Retrieve (GET): http://0.0.0.0:8000/api/bill-submissions/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bill-submissions/{id}/
dushanbe_router.register('bill-submissions', BillSubmissionViewSet)


# APIView
urlpatterns = [

]

