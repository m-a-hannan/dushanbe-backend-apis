from dushanbe.models import Type
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Type Create Serializer
class TypeCreateSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(max_length=250, validators=[UniqueValidator(queryset=Type.objects.all())])

    class Meta:
        model = Type
        fields = ('id', 'type_name')


# Type Update Serializer
class TypeUpdateSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(required=False, max_length=250, validators=[UniqueValidator(queryset=Type.objects.all())])

    class Meta:
        model = Type
        fields = ('id', 'type_name')


# Type List Serializer
class TypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type_name')


