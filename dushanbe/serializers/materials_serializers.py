# from rest_framework import serializers
# from dushanbe.models import Bill, Topic, Material
# from rest_framework.validators import UniqueValidator
#
#
# # Material Create Serializer
# class MaterialCreateSerializer(serializers.ModelSerializer):
#     material_name = serializers.CharField(max_length=None)
#     item_serial_no = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=Material.objects.all())])
#     unit = serializers.CharField(max_length=10)
#     quantity = serializers.DecimalField(decimal_places=2, max_digits=8)
#
#     class Meta:
#         model = Material
#         fields = ('id', 'material_name', 'item_serial_no', 'unit', 'quantity', 'active_status')
#
#
# # Material Update Serializer
# class MaterialUpdateSerializer(serializers.ModelSerializer):
#     material_name = serializers.CharField(required=False, max_length=None)
#     item_serial_no = serializers.CharField(required=False, max_length=20, validators=[UniqueValidator(queryset=Material.objects.all())])
#     unit = serializers.CharField(required=False, max_length=10)
#     quantity = serializers.DecimalField(required=False, decimal_places=2, max_digits=8)
#
#     class Meta:
#         model = Material
#         fields = ('id', 'material_name', 'item_serial_no', 'unit', 'quantity', 'active_status')
#
#
# # Material List Serializer
# class MaterialListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Material
#         fields = ('id', 'material_name', 'item_serial_no', 'unit', 'quantity', 'active_status')
#
#
