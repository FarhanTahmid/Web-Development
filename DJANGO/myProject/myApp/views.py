from multiprocessing import context
from .models import Feature
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    feature1=Feature()
    feature1.name='Farhan'
    feature1.id=10
    feature1.description="A very good boy"
    context={
        'name':'farhan',
        'age':22,
        'nationality':'Bangladeshi',
    }
    return render(request,'index.html',context,{'feature':feature1})
