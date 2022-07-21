import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def showpage(request):
    return render(request,'database.html')