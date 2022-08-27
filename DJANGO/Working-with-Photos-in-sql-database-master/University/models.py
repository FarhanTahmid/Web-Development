from distutils.archive_util import make_zipfile
from distutils.command.upload import upload
from enum import Flag
from hashlib import blake2b
from operator import mod
from pickle import FALSE
from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import User

# Create your models here.

class OfferedCourse(models.Model):
    id=models.CharField(max_length=50,primary_key=True,null=False,blank=False,verbose_name="Course ID")
    name=models.CharField(max_length=100,null=False,blank=False,verbose_name="Course Name")
    description=models.CharField(max_length=150,null=False,blank=True,verbose_name="Description")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentList(models.Model):
    id=models.CharField(max_length=20,primary_key=True,null=False,blank=FALSE,verbose_name="Student Id")
    fullname=models.CharField(max_length=50,null=False,verbose_name="Full Name")
    email=models.CharField(max_length=50,null=False,verbose_name="Email")


class Grade(models.Model):
    course_id=models.CharField(max_length=20,null=False,blank=FALSE,verbose_name="Course Id")
    result=models.CharField(max_length=50,null=False,verbose_name="Result")
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class CourseRegistrations(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course_ID=models.CharField(max_length=50,null=False,verbose_name="Course ID")
    course_Name=models.CharField(max_length=50,null=False,verbose_name="Course Name")
    course_Description=models.CharField(max_length=50,null=False,verbose_name="Course Description")

class Complains(models.Model):
    name=models.CharField(max_length=50,null=False,verbose_name="Bull Name",primary_key=True)
    contact=models.CharField(max_length=15,null=False,verbose_name="Contact No")
    email=models.CharField(max_length=30,verbose_name="E mail")
    facebookid=models.CharField(max_length=100,verbose_name="Facebook ID")
    instaid=models.CharField(max_length=100,verbose_name="Instagram ID")
    linkedinid=models.CharField(max_length=100,verbose_name="Linkedin ID")
    snapid=models.CharField(max_length=100,verbose_name="Snapchat ID")
    prove=models.ImageField(upload_to='proves/')

class Image(models.Model):
    name= models.CharField(max_length=500)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)
    