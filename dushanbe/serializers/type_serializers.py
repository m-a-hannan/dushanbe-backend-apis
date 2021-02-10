from rest_framework import serializers
from dushanbe.models import Type, Material


""" Extra Serializers for Type Serializers """


# Material Serializer
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'short_material_name', 'serial_no', 'unit', 'quantity')


""" Type Serializers """


# Type Create Serializer
class TypeCreateSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(max_length=250)
    material = serializers.PrimaryKeyRelatedField(many=False, queryset=Material.objects.all())

    class Meta:
        model = Type
        fields = ('id', 'type_name', 'material')


# Type Update Serializer
class TypeUpdateSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(required=False, max_length=250)
    material = serializers.PrimaryKeyRelatedField(required=False, many=False, queryset=Material.objects.all())

    class Meta:
        model = Type
        fields = ('id', 'type_name', 'material')


# Type List Serializer
class TypeListSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'type_name', 'material')


