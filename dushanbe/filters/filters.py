from django_filters import rest_framework as filters
from dushanbe.models import Bill, Type, Material, WorkSubmission


# Bill
# Filter (GET): http://127.0.0.1:8000/api/bills/?id=1
class BillFilter(filters.FilterSet):
    class Meta:
        model = Bill
        fields = ['id']


# Type
# Filter (GET): http://127.0.0.1:8000/api/types/?id=1&bill=1
class TypeFilter(filters.FilterSet):
    class Meta:
        model = Type
        fields = ['id', 'bill']


# Material
# Filter (GET): http://127.0.0.1:8000/api/materials/?id=1&type=1&serial_no=42&unit=nr&quantity=63.00
class MaterialFilter(filters.FilterSet):
    class Meta:
        model = Material
        fields = ['id', 'type', 'serial_no', 'unit', 'quantity']


# WorkSubmission
# Filter (GET):
# http://127.0.0.1:8000/api/work-submissions/?
# id=2&bill=2&type=2&material=2&serial_no=97&unit=kits&quantity=3.69&submission_date=1998-09-22&work_progress=79&created_by=3
class WorkSubmissionFilter(filters.FilterSet):
    serial_no = filters.NumberFilter(field_name="material__serial_no")
    unit = filters.CharFilter(field_name="material__unit")
    quantity = filters.CharFilter(field_name="material__quantity")

    class Meta:
        model = WorkSubmission
        fields = ['id', 'bill', 'type', 'material', 'serial_no', 'unit', 'quantity', 'submission_date', 'work_progress', 'created_by']

