from django.contrib import admin
from .models import Bill, Material, NameOfWork


admin.site.site_header = "Dushanbe Admin"


# NameOfWork Inline
class NameOfWorkInline(admin.StackedInline):
    model = NameOfWork


# Bill
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill_name', 'created_by', 'created_datetime', 'active_status']
    list_display_links = ['bill_name']
    list_editable = ['active_status']
    list_filter = ['created_by']
    inlines = [NameOfWorkInline, ]


# Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_name']
    list_display_links = ['material_name']


# NameOfWork
@admin.register(NameOfWork)
class NameOfWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_name', 'bill', 'material', 'item_serial_no', 'unit', 'quantity', 'submission_date', 'work_progress']
    list_display_links = ['work_name']
    list_filter = ['bill', 'material']




