from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# ContentType serializers
class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ('app_label', 'model')


# Permission serializers
class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(many=False)

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename', 'content_type')

