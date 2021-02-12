from rest_framework import serializers
from dushanbe.models import Bill, Type


""" Extra Serializers for This Serializers """


# Bill Serializer
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'short_bill_name')


""" This Serializers """


# Type Create Serializer
class TypeCreateSerializer(serializers.ModelSerializer):
    bill = serializers.PrimaryKeyRelatedField(many=False, queryset=Bill.objects.all())
    type_name = serializers.CharField(max_length=250)

    class Meta:
        model = Type
        fields = ('id', 'bill', 'short_type_name', 'type_name')


# Type Update Serializer
class TypeUpdateSerializer(serializers.ModelSerializer):
    bill = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Bill.objects.all())
    type_name = serializers.CharField(required=False, max_length=250)

    class Meta:
        model = Type
        fields = ('id', 'bill', 'short_type_name', 'type_name')


# Type List Serializer
class TypeListSerializer(serializers.ModelSerializer):
    bill = BillSerializer(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'bill', 'short_type_name', 'type_name')


