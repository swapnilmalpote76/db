from django.db import models
from django.forms import forms

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=30 )
    address=models.CharField(max_length=100 , default="" )
    status=models.BooleanField(default=False)
    salary=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
