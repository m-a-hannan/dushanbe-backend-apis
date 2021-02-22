from django.contrib import admin
from django.contrib.auth.models import User, Group

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
    list_display_links = ['id']
    filter_horizontal = ['permissions']
    ordering = ['-id']

    def permissions_list(self, obj):
        return " | ".join([i.codename for i in obj.permissions.all()])
