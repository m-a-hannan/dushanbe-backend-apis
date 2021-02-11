from rest_framework import serializers
from dushanbe.models import Bill, Type, Material
from rest_framework.validators import UniqueValidator


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


""" This Serializers """


# Material Create Serializer
class MaterialCreateSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())
    material_name = serializers.CharField(max_length=None)
    serial_no = serializers.IntegerField()
    unit = serializers.CharField(max_length=10)
    quantity = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Material
        fields = ('id', 'type', 'short_material_name', 'material_name', 'serial_no', 'unit', 'quantity')


# Material Update Serializer
class MaterialUpdateSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Type.objects.all())
    material_name = serializers.CharField(required=False, max_length=None)
    serial_no = serializers.IntegerField(required=False, validators=[UniqueValidator(queryset=Material.objects.all())])
    unit = serializers.CharField(required=False, max_length=10)
    quantity = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)

    class Meta:
        model = Material
        fields = ('id', 'type', 'short_material_name', 'material_name', 'serial_no', 'unit', 'quantity')


# Material List Serializer
class MaterialListSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Material
        fields = ('id', 'type', 'short_material_name', 'material_name', 'serial_no', 'unit', 'quantity')



