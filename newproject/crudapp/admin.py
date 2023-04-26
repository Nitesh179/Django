from django.contrib import admin
from crudapp.models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'desg', 'age', 'doj']
