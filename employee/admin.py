from django.contrib import admin
from employee.models import Employee


# Registerd Employee Model here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'empid', 'city']
