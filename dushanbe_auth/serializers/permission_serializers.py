from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


""" Extra Serializers for This Serializers """


# ContentType serializers
class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ('app_label', 'model')


""" This Serializers """


# Permission serializers
class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(many=False)

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename', 'content_type')

