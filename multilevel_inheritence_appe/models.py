from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    salary=models.FloatField()

class Customer(Employee):
    cust_name=models.CharField(max_length=50)
    sales=models.FloatField()

class Student(Customer):
    stu_name=models.CharField(max_length=50)
    marks=models.FloatField()

