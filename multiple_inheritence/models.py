from django.db import models

# Create your models here.


class Customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=50)
    sales=models.FloatField()

class Student(models.Model):
    stu_id=models.AutoField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    marks=models.FloatField()

class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=50)
    salary=models.FloatField()
class Product(Customer,Student,Employee):
    P_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=50)
    p_price=models.FloatField()