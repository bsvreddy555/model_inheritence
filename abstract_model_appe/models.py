from django.db import models

# Create your models here.


class common_data(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    class Meta:
        abstract = True

class Employee(common_data):
    salary=models.FloatField()

class Customer(common_data):
    sales=models.IntegerField()

class Student(common_data):
    marks=models.FloatField()

