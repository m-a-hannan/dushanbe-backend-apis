from django_filters import rest_framework as filters
from dushanbe.models import Bill, Type, Material, BillSubmission


# Filter (GET): http://127.0.0.1:8000/api/bill-submissions/?
# bill=1&type=1&material=2&serial_no=2&unit=kits&quantity=1.00&submission_date=2021-02-07&work_progress=2&created_by=1
class BillSubmissionFilter(filters.FilterSet):
    serial_no = filters.NumberFilter(field_name="material__serial_no")
    unit = filters.CharFilter(field_name="material__unit")
    quantity = filters.NumberFilter(field_name="material__quantity")

    class Meta:
        model = BillSubmission
        fields = ['bill', 'type', 'material', 'serial_no', 'unit', 'quantity', 'submission_date', 'work_progress', 'created_by']


