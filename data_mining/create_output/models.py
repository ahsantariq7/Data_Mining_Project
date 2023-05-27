# Create your models here.
from django.db import models

class Student(models.Model):  
    firstname = models.CharField(max_length=100)  
    lastname  = models.CharField(max_length=100)  
    email     = models.EmailField()  
    file      = models.FileField() 

