from django.contrib import admin
from employees.models import Employee

@admin.register(Employee)
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=[ 'id', 'propic','uploaded_at', 'name', 'dob', 'email']
   