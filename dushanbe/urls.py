from django.urls import path
from rest_framework import routers
from dushanbe.views.bill_views import BillViewSet
# from dushanbe.views.topic_views import TopicViewSet
# from dushanbe.views.materials_views import MaterialViewSet

# ModelViewSet router
dushanbe_router = routers.DefaultRouter()

""" Bill Routers """
# Create (POST): http://0.0.0.0:8000/api/bills/
# List (GET): http://0.0.0.0:8000/api/bills/
# Retrieve (GET): http://0.0.0.0:8000/api/bills/{id}/
# Update (PUT): http://127.0.0.1:8000/api/bills/{id}/
# Delete (DELETE): http://127.0.0.1:8000/api/bills/{id}/
dushanbe_router.register('bills', BillViewSet)

# """ Topic Routers """
# # Create (POST): http://0.0.0.0:8000/api/topics/
# # List (GET): http://0.0.0.0:8000/api/topics/
# # Retrieve (GET): http://0.0.0.0:8000/api/topics/{id}/
# # Update (PUT): http://127.0.0.1:8000/api/topics/{id}/
# # Delete (DELETE): http://127.0.0.1:8000/api/topics/{id}/
# dushanbe_router.register('topics', TopicViewSet)
#
# """ Material Routers """
# # Create (POST): http://0.0.0.0:8000/api/materials/
# # List (GET): http://0.0.0.0:8000/api/materials/
# # Retrieve (GET): http://0.0.0.0:8000/api/materials/{id}/
# # Update (PUT): http://127.0.0.1:8000/api/materials/{id}/
# # Delete (DELETE): http://127.0.0.1:8000/api/materials/{id}/
# dushanbe_router.register('materials', MaterialViewSet)

# APIView
urlpatterns = [

]

