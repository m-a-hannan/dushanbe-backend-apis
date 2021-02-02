# from django.db import transaction
# from django.db.models import Count, Q
# from rest_framework import status, viewsets
# from rest_framework.response import Response
#
# # app
# from dushanbe.models import Material
# from dushanbe.paginations.paginations import CustomPageNumberPagination
# from dushanbe.permissions.common_permissions import DjangoModelPermissionsWithGET
# from dushanbe.serializers.materials_serializers import (
#     MaterialCreateSerializer,
#     MaterialUpdateSerializer,
#     MaterialListSerializer
# )
#
#
# # Create (POST): http://0.0.0.0:8000/api/materials/
# # List (GET): http://0.0.0.0:8000/api/materials/
# # Retrieve (GET): http://0.0.0.0:8000/api/materials/{id}/
# # Update (PUT): http://127.0.0.1:8000/api/materials/{id}/
# # Delete (DELETE): http://127.0.0.1:8000/api/materials/{id}/
# class MaterialViewSet(viewsets.ModelViewSet):
#     queryset = Material.objects.all().order_by('material_name')
#     serializer_class = MaterialListSerializer
#     permission_classes = (DjangoModelPermissionsWithGET, )
#     pagination_class = CustomPageNumberPagination
#
#     @transaction.atomic
#     def create(self, request, *args, **kwargs):
#         serializer = MaterialCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     @transaction.atomic
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = MaterialUpdateSerializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
