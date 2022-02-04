from django.db import models

# Create your models here.



class student_affairs(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email =models.EmailField(max_length=40)
    
    
class Intake(models.Model):
    id=models.AutoField(primary_key=True)
    intake_name=models.CharField(max_length=20)
    start_date =models.DateField()
    end_date =models.DateField()
    
class track(models.Model):
    id=models.AutoField(primary_key=True)
    track_name=models.CharField(max_length=20)
    



