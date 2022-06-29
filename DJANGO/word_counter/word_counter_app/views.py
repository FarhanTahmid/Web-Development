from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form(request):
    return render(request,'form.html')
def counter(request):
    words=request.GET['words']
    amountOfWords=len(words.split())
    return render(request,'counter.html',{'amount':amountOfWords})