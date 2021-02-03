from django.contrib import admin
from .models import Bill, Material, WorkType, Work


admin.site.site_header = "Dushanbe Admin"


# Work Inline
# class WorkInline(admin.StackedInline):
class WorkInline(admin.TabularInline):
    model = Work


# Bill
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill_name', 'created_by', 'created_datetime', 'active_status']
    list_display_links = ['bill_name']
    list_editable = ['active_status']
    list_filter = ['created_by']
    inlines = [WorkInline, ]


# Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_name']
    list_display_links = ['material_name']


# WorkType
@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_type_name']
    list_display_links = ['work_type_name']


# Work
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'bill', 'work_type', 'material', 'item_serial_no', 'unit', 'quantity',
        'submission_date', 'work_progress'
    ]
    list_display_links = ['bill']
    list_filter = ['bill', 'work_type', 'material']




