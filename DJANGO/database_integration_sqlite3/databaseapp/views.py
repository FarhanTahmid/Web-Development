import re
import sqlite3
from urllib import request
from django.shortcuts import render
from django.db import connections


from databaseapp.models import userList
    
# Create your views here.
def showpage(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        phoneNumber=request.POST['phoneNumber']
        address=request.POST['address']


        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO databaseapp_userlist (name,username,email,phoneNumber,address) VALUES('"+fullname+"','"+username+"','"+email+"','"+phoneNumber+"','"+address+"')")
        try:
            db_cursor.execute("CREATE TABLE ungabunga (person varchar(50))")
        except sqlite3.OperationalError as e:
            print("Error occured: ",e)

    return render(request,'signUpForm.html')