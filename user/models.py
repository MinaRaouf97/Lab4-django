import email
from statistics import mode
from django.db import models

# Create your models here.



class affairs_user(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    password = models.CharField(max_length=30)


