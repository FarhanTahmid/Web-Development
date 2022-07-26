from importlib.util import set_loader
from tabnanny import verbose
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.text
class userList(models.Model):
    name=models.CharField(max_length=30,null=False,blank=False, verbose_name="Full name")
    username=models.CharField(max_length=15,primary_key=True ,null=False,blank=False,verbose_name="User name")
    email=models.CharField(max_length=40,null=False,blank=False, verbose_name="Email")
    phoneNumber=models.CharField(max_length=30,null=False,blank=False, verbose_name="Phone number")
    address=models.CharField(max_length=60,null=False,blank=False, verbose_name="Address")
    