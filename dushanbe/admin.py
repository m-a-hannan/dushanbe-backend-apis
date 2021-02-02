from .models import Bill
from django.contrib import admin


admin.site.site_header = "Dushanbe Admin"


# Bill
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'bill_name', 'topic_name', 'material_name', 'item_serial_no', 'unit', 'quantity', 'submission_date',
        'work_progress', 'active_status'
    ]
    list_display_links = ['bill_name']
    list_editable = ['active_status']


# # Topic
# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ['id', 'topic_name', 'active_status']
#     list_display_links = ['topic_name']
#     list_editable = ['active_status']
#
#
# # Material
# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     list_display = ['id', 'material_name', 'item_serial_no', 'unit', 'quantity', 'active_status']
#     list_display_links = ['material_name']
#     list_editable = ['active_status']








