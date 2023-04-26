from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    desg=models.CharField(max_length=200)
    age=models.IntegerField()
    doj=models.DateField()


