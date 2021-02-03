from dushanbe.models import Bill
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_superuser')


# Bill Create Serializer
class BillCreateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(max_length=500,  validators=[UniqueValidator(queryset=Bill.objects.all())])
    created_by = UserSerializer(required=False, read_only=True)
    created_datetime = serializers.DateTimeField(required=False, format="%Y-%m-%d %I:%M %p")

    class Meta:
        model = Bill
        fields = ('id', 'bill_name', 'created_by', 'created_datetime', 'active_status')


# Bill Update Serializer
class BillUpdateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(required=False, max_length=500,  validators=[UniqueValidator(queryset=Bill.objects.all())])
    created_by = UserSerializer(required=False, read_only=True)
    created_datetime = serializers.DateTimeField(required=False, format="%Y-%m-%d %I:%M %p")

    class Meta:
        model = Bill
        fields = ('id', 'bill_name', 'created_by', 'created_datetime', 'active_status')


# Bill List Serializer
class BillListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_datetime = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p")

    class Meta:
        model = Bill
        fields = ('id', 'bill_name', 'created_by', 'created_datetime', 'active_status')




