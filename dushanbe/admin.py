from django.contrib import admin
from .models import Bill, Material, Type, WorkSubmission

admin.site.site_header = "Dushanbe Admin"


# Bill
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill_name']
    list_display_links = ['id']
    ordering = ['-id']


# Type
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill', 'type_name']
    list_display_links = ['id']
    list_filter = ['bill']
    ordering = ['-id']


# Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_bill_name', 'type', 'material_name', 'serial_no', 'unit', 'quantity']
    list_display_links = ['id']
    list_filter = ['type']
    ordering = ['-id']


# WorkSubmission
@admin.register(WorkSubmission)
class WorkSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'bill', 'type', 'material', 'serial_no', 'unit', 'quantity', 'submission_date', 'work_progress',
        'created_by', 'active_status'
    ]
    list_filter = ['created_by', 'bill', 'type', 'material']
    list_editable = ['active_status']
    list_display_links = ['id']
    ordering = ['-id']
