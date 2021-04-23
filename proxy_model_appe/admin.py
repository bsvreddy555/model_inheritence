from django.contrib import admin
from .models import Student,Student_Proxy

# Register your models here.

class Admin_Student(admin.ModelAdmin):
    list_display = ['name','location','marks']

class Admin_student_proxy(admin.ModelAdmin):
    list_display = ['name','location','marks']

admin.site.register(Student,Admin_Student)
admin.site.register(Student_Proxy,Admin_student_proxy)
