from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Bill, Material, Type, BillSubmission


admin.site.site_header = "Dushanbe Admin"


# User
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
        'groups_list', 'permissions'
    ]
    list_display_links = ['username']
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['id']

    def groups_list(self, obj):
        return " | ".join([i.name for i in obj.groups.all()])

    def permissions(self, obj):
        return " | ".join([i.codename for i in obj.user_permissions.all()])


# Group
admin.site.unregister(Group)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'permissions_list']
    list_display_links = ['name']
    filter_horizontal = ['permissions']
    ordering = ['-id']

    def permissions_list(self, obj):
        return " | ".join([i.codename for i in obj.permissions.all()])


# BillSubmission Inline
# class BillSubmissionInline(admin.StackedInline):
class BillSubmissionInline(admin.TabularInline):
    model = BillSubmission


# Bill
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill_name', 'active_status']
    list_display_links = ['bill_name']
    ordering = ['-id']
    # inlines = [BillSubmissionInline, ]


# Type
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']
    list_display_links = ['type_name']
    ordering = ['-id']


# Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_name', 'serial_no', 'unit', 'quantity']
    list_display_links = ['material_name']
    ordering = ['-id']


# BillSubmission
@admin.register(BillSubmission)
class BillSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'bill', 'type', 'material', 'serial_no', 'unit', 'quantity', 'submission_date',
        'work_progress', 'created_by'
    ]
    list_display_links = ['bill']
    # list_filter = ['bill', 'type', 'material']
    ordering = ['-id']






