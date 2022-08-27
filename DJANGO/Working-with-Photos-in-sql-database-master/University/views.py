
from pdb import line_prefix
from sqlite3 import Cursor
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import models

from .models import OfferedCourse, Grade, CourseRegistrations,Image

from . import courseadd
from .import studentRegistration
from django.db import connections



# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def login(request):
    if request.method=='POST':
        username=request.POST['id']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('University:menu')
        else:
            messages.info(request,'Credentials given are wrong')
            return redirect('University:login')
    else:
        return render(request,'login.html')

def signUp(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['id']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('University:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'ID already exists')
                return redirect('University:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                student=studentRegistration.StudentAdd(username,fullname,email)
                student.addStudent()
                return redirect('University:login')
                


        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('University:signup')
    else:
         return render(request, 'sign_up.html')
     
@login_required
def menu(request):
    return render(request,"menu.html")

@login_required
def course_add(request):
    if request.method=='POST':
        bullyname=request.POST['bullyname']
        contact=request.POST['contact']
        email=request.POST['email']
        facebookLink=request.POST['facebookLink']
        instaLink=request.POST['instaLink']
        linkedinLink=request.POST['linkedinLink']
        snapLink=request.POST['snapLink']
        
        file=request.FILES.get('myfile')
        print(type(file))
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("INSERT INTO University_complains (name,contact,email,facebookid,instaid,linkedinid,snapid,prove) VALUES('"+bullyname+"','"+contact+"','"+email+"','"+facebookLink+"','"+instaLink+"','"+linkedinLink+"','"+snapLink+"','"+file+"')")
        
    return render(request, 'course_add.html')

@login_required
def course_drop(request):
    if request.method=='POST':
        id=request.POST['courseID']
        course=courseadd.CourseAdd(id)
        course.deleteCourse()
    
    return render(request,'course_drop.html')

@login_required
def course_registration(request):
    data = serializers.serialize("python",OfferedCourse.objects.all())
    context = {
        'data':data,
    }
    return render(request, 'course_registration.html', context)

@login_required
def personal_information(request):
    courses = CourseRegistrations.objects.filter(owner=request.user)
    context = {'courses':courses}
    return render(request, 'personal_information.html',context)

@login_required
def results(request):
    grades = Grade.objects.filter(owner=request.user).order_by('date_added')
    context = {'grades':grades}
    return render(request, 'results.html',context)

def image(request):
    
    if request.method=="POST":
        file=request.FILES['files']
        image=Image.objects.get(name="farhan2")
            
        image.save()
    
    # context= {'imagefile': file,
              
    # }
    return render(request,'image.html')

