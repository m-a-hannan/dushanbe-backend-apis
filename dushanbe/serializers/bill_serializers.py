from dushanbe.models import Bill
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Bill Create Serializer
class BillCreateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(max_length=500)
    topic_name = serializers.CharField(max_length=250)
    material_name = serializers.CharField(max_length=None)
    item_serial_no = serializers.CharField(max_length=20)
    unit = serializers.CharField(max_length=10)
    quantity = serializers.DecimalField(decimal_places=2, max_digits=8)
    submission_date = serializers.DateField(format="%Y-%m-%d")
    work_progress = serializers.IntegerField(default=0)

    class Meta:
        model = Bill
        fields = (
            'id', 'bill_name', 'topic_name', 'material_name', 'item_serial_no', 'unit', 'quantity', 'submission_date',
            'work_progress', 'active_status'
        )


# Bill Update Serializer
class BillUpdateSerializer(serializers.ModelSerializer):
    bill_name = serializers.CharField(required=False, max_length=500)
    topic_name = serializers.CharField(required=False, max_length=250)
    material_name = serializers.CharField(required=False, max_length=None)
    item_serial_no = serializers.CharField(required=False, max_length=20)
    unit = serializers.CharField(required=False, max_length=10)
    quantity = serializers.DecimalField(required=False, decimal_places=2, max_digits=8)
    submission_date = serializers.DateField(required=False, format="%Y-%m-%d")
    work_progress = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Bill
        fields = (
            'id', 'bill_name', 'topic_name', 'material_name', 'item_serial_no', 'unit', 'quantity', 'submission_date',
            'work_progress', 'active_status'
        )


# Bill List Serializer
class BillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = (
            'id', 'bill_name', 'topic_name', 'material_name', 'item_serial_no', 'unit', 'quantity', 'submission_date',
            'work_progress', 'active_status'
        )




