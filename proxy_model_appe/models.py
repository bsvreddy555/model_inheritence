from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    marks=models.FloatField()

class Student_Proxy(Student):
    class Meta:
        proxy = True

