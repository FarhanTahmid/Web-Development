from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userRegistration(request):
    return render(request,'userRegistration.html')