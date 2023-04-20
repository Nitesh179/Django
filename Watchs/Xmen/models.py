from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=12)
    msg=models.TextField()
    dob=models.DateField()
   
   
    def __str__(self):
        return self.name


class Customer(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    address=models.TextField()
    phone=models.CharField(max_length=12)


    def __str__(self):
        return self.name