from django.contrib import admin

from .models import Employee
from .models import Group
from .models import Section
from .models import Division
from .models import Status


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'phone', 'status_name',
                    'notes', 'returning', 'site_phone', 'site', 'schedule',
                    'section_name', 'group_name', 'user']

    class Meta:
        model = Employee

    def section_name(self, obj):
        return obj.section.name

    section_name.admin_order_field = 'name'

    def group_name(self, obj):
        return obj.group.name

    group_name.admin_order_field = 'name'

    def status_name(selfself, obj):
        return obj.status.desc

    status_name.admin_order_field = 'desc'


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'division_name']

    def division_name(self, obj):
        return obj.division.name

    division_name.admin_order_field = 'name'


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc', 'statusId']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Status, StatusAdmin)
