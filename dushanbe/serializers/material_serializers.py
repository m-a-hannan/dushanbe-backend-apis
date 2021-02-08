from dushanbe.models import Material
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Material Create Serializer
class MaterialCreateSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(max_length=None)
    serial_no = serializers.IntegerField(validators=[UniqueValidator(queryset=Material.objects.all())])
    unit = serializers.CharField(max_length=10)
    quantity = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Material
        fields = ('id', 'material_name', 'serial_no', 'unit', 'quantity')


# Material Update Serializer
class MaterialUpdateSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(required=False, max_length=None)
    serial_no = serializers.IntegerField(required=False, validators=[UniqueValidator(queryset=Material.objects.all())])
    unit = serializers.CharField(required=False, max_length=10)
    quantity = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)

    class Meta:
        model = Material
        fields = ('id', 'material_name', 'serial_no', 'unit', 'quantity')


# Material List Serializer
class MaterialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'short_material_name', 'serial_no', 'unit', 'quantity')



