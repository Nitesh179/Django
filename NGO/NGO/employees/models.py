from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Create your models here.

class Employee(models.Model):
    propic=models.FileField(upload_to="images/",null=True, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    name=models.CharField(max_length=150)
    dob=models.DateField()
    contact=models.IntegerField()
    email=models.EmailField()

    maritialstatus=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip=models.IntegerField()
    address=models.CharField(max_length=100)

    bankname=models.CharField(max_length=100)
    accountno=models.IntegerField()
    branch=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=100,validators=[alphanumeric])

    feedback=models.CharField(max_length=100)

    def __str__(self):  
        return self.name
    

