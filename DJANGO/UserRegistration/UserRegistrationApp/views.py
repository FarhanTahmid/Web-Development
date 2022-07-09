from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def userRegistration(request):

    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('homepage')
        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('register')
    else:
        return render(request,'userRegistration.html')

def homepage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('logged_in')
        else:
            messages.info(request,'Credentials given are Wrong!')
            return redirect('homepage')
    else:
        return render(request,'homepage.html')

def logged_in(request):
    return render(request,'loggedin.html')
def logout(request):
    auth.logout(request)
    return redirect('register')
def post(request,pk):
    return render(request,'post.html',{'pk':pk})