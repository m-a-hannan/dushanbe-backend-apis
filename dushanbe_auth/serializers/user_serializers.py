from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


""" Extra Serializers for This Serializers """


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


# Group serializers
class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


""" This Serializers """


# User login response serializers
class UserLoginResponseSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = ['groups', 'user_permissions']
