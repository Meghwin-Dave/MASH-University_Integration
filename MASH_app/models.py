
from doctest import master
from email import message
import email
from time import time
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Contactd (models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=255)


class Newsletter(models.Model):
    email=models.CharField(max_length=50)

# Models for User
class Role(models.Model):
    Role = models.CharField(max_length=50)

    class Meta:
        db_table = 'Role'

    def __str__(self):
        return self.Role


class Master(models.Model):
    
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)
    IsActive = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = 'Master'

    def __str__(self):
        return self.Email

class User(models.Model):
    Master = models.ForeignKey(Master,on_delete=models.CASCADE)
    UID = models.CharField(max_length=25)
    FullName = models.CharField(max_length=25, default='')
    Enrollment = models.CharField(max_length=12)

    class Meta: 
        db_table = 'User'

    def __str__(self) -> str:
        return self.Enrollment

class Faculty(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=25, default='')
    class Meta: 
        db_table = 'Faculty' 
    
    def __str__(self):
        return self.FullName

class Assign(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    assign = models.FileField(upload_to="assignments/", default="xyz.png")
    class Meta: 
        db_table = 'Assign'

class Video(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    video=models.CharField(max_length=550)
    class Meta: 
        db_table = 'Video'
    

class Note(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    note=models.CharField(max_length=550) 
    class Meta: 
        db_table = 'Note '

class Feedback(models.Model):
   Master = models.ForeignKey(Master, on_delete=models.CASCADE)
   First = models.CharField(max_length=256) 
   Last = models.CharField(max_length=256) 
   Subject = models.CharField(max_length=256) 
   Feedback = models.CharField(max_length=256) 
   emailf = models.EmailField(max_length=50)
   enrollmentf = models.IntegerField(max_length=12)
