from dushanbe.models import Bill
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


# Bill Create Serializer
class BillCreateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(max_length=500, validators=[UniqueValidator(queryset=Bill.objects.all())])

    class Meta:
        model = Bill
        fields = ('id', 'short_bill_name', 'bill_name')


# Bill Update Serializer
class BillUpdateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(required=False, max_length=500, validators=[UniqueValidator(queryset=Bill.objects.all())])

    class Meta:
        model = Bill
        fields = ('id', 'short_bill_name', 'bill_name')


# Bill List Serializer
class BillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'short_bill_name', 'bill_name')

