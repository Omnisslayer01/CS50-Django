from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function(request):
    return HttpResponse("Hello World!")

def hi(request):
    return HttpResponse("Hi, Diyan")

def Zawardo(request, name):
    return render(request,"home/DIO.html",{
        "name":name
    })

def greet(request,name):
    return HttpResponse(f"Hello, {name}")
