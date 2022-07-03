from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    feature1=Feature()
    feature1.id=10
    feature1.name="Farhan"
    feature1.detail="Web developer"

    return render(request,'index.html',{'feature':feature1})