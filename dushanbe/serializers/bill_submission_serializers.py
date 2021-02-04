from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from dushanbe.models import Bill, Material, Type, BillSubmission


""" Extra Serializers for BillSubmission Serializers """


# Bill Serializer
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'bill_name', 'active_status')


# Type Serializer
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type_name')


# Material Serializer
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'material_name', 'serial_no', 'unit', 'quantity')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_superuser')


""" BillSubmission Serializers """


# BillSubmission Create Serializer
class BillSubmissionCreateSerializer(serializers.ModelSerializer):
    bill = serializers.PrimaryKeyRelatedField(many=False, queryset=Bill.objects.all())
    # bill = BillSerializer(required=False, read_only=True)

    type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())
    # type = TypeSerializer(required=False, read_only=True)

    material = serializers.PrimaryKeyRelatedField(many=False, queryset=Material.objects.all())
    # material = MaterialSerializer(required=False, read_only=True)

    submission_date = serializers.DateField(required=False, format="%Y-%m-%d")
    work_progress = serializers.IntegerField(default=0)

    class Meta:
        model = BillSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by')


# BillSubmission Update Serializer
class BillSubmissionUpdateSerializer(serializers.ModelSerializer):
    # bill = serializers.PrimaryKeyRelatedField(many=False, queryset=Bill.objects.all())
    bill = BillSerializer(required=False, read_only=True)

    # type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())
    type = TypeSerializer(required=False, read_only=True)

    # material = serializers.PrimaryKeyRelatedField(many=False, queryset=Material.objects.all())
    material = MaterialSerializer(required=False, read_only=True)

    submission_date = serializers.DateField(required=False, format="%Y-%m-%d")
    work_progress = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = BillSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by')


# BillSubmission List Serializer
class BillSubmissionListSerializer(serializers.ModelSerializer):
    bill = BillSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    submission_date = serializers.DateField(format="%Y-%m-%d")
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = BillSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by')








