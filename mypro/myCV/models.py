from django.db import models

# Create your models here.


class Signup(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    email=models.EmailField()
    
class Login(models.Model):
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=8)
    type = models.IntegerField()
    
    
class Profile(models.Model):
    username = models.ForeignKey(Signup, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    school=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    skills=models.TextField(max_length=1000)
    about_you=models.TextField(max_length=1000)
    previous_work=models.TextField(max_length=1000)
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    