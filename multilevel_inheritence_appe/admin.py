from django.contrib import admin
from .models import Employee,Customer,Student

# Register your models here.


class Admin_Employee(admin.ModelAdmin):
    list_display = ['emp_name','salary']

class Admin_Customer(admin.ModelAdmin):
    list_display = ['cust_name','sales','cust_name','sales']

class Admin_Student(admin.ModelAdmin):
    list_display = ['stu_name','marks']


admin.site.register(Employee,Admin_Employee)
admin.site.register(Customer,Admin_Customer)
admin.site.register(Student,Admin_Student)