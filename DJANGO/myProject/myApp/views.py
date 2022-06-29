from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        'name':'farhan',
        'age':22,
        'nationality':'Bangladeshi',
    }
    return render(request,'index.html',context)
