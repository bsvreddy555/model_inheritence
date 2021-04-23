from django.contrib import admin
from .models import Student,Customer,Employee

# Register your models here.

class Admin_Employee(admin.ModelAdmin):
    list_display = ['name','location','salary']

class Admin_Customer(admin.ModelAdmin):
    list_display = ['name','location','sales']

class Admin_Student(admin.ModelAdmin):
    list_display = ['name','location','marks']

admin.site.register(Employee,Admin_Employee)
admin.site.register(Customer,Admin_Customer)
admin.site.register(Student,Admin_Student)
