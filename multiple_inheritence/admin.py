from django.contrib import admin
from  .models import Customer,Employee,Student,Product

# Register your models here.



class Admin_Customer(admin.ModelAdmin):
    list_display = ['cust_id','cust_name','sales']

class Admin_Student(admin.ModelAdmin):
    list_display = ['stu_id','stu_name','marks']

class Admin_Employee(admin.ModelAdmin):
    list_display = ['emp_id','emp_name','salary']

class Admin_Product(admin.ModelAdmin):
    list_display = ['P_id','p_name','p_price']

admin.site.register(Customer,Admin_Customer)
admin.site.register(Student,Admin_Student)
admin.site.register(Employee,Admin_Employee)
admin.site.register(Product,Admin_Product)
