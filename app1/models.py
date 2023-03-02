
from django.db import models

class SignUp(models.Model):
    Name=models.CharField(max_length=20)
    Place=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=8)

class Gallery(models.Model):
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Name=models.CharField(max_length=20)
    Brand=models.CharField(max_length=20)
    



# Create your models here.
