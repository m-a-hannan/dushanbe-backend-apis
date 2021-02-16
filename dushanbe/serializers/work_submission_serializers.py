from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from dushanbe.models import Bill, Material, Type, WorkSubmission


""" Extra Serializers for This Serializers """


# Bill Serializer
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'short_bill_name')


# Type Serializer
class TypeSerializer(serializers.ModelSerializer):
    bill = BillSerializer(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'bill', 'short_type_name')


# Material Serializer
class MaterialSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Material
        fields = ('id', 'type', 'short_material_name', 'serial_no', 'unit', 'quantity')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_superuser')


""" This Serializers """


# WorkSubmission Create Serializer
class WorkSubmissionCreateSerializer(serializers.ModelSerializer):
    bill = serializers.PrimaryKeyRelatedField(many=False, queryset=Bill.objects.all())
    type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())
    material = serializers.PrimaryKeyRelatedField(many=False, queryset=Material.objects.all())
    submission_date = serializers.DateField(format="%Y-%m-%d")
    work_progress = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = WorkSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by', 'active_status')


# WorkSubmission Update Serializer
class WorkSubmissionUpdateSerializer(serializers.ModelSerializer):
    bill = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Bill.objects.all())
    type = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Type.objects.all())
    material = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Material.objects.all())
    submission_date = serializers.DateField(required=False, format="%Y-%m-%d")
    work_progress = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)

    class Meta:
        model = WorkSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by', 'active_status')


# WorkSubmission List Serializer
class WorkSubmissionListSerializer(serializers.ModelSerializer):
    bill = BillSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    submission_date = serializers.DateField(format="%Y-%m-%d")
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = WorkSubmission
        fields = ('id', 'bill', 'type', 'material', 'submission_date', 'work_progress', 'created_by', 'active_status')









