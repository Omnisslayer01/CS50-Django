from django.shortcuts import render
import datetime
from django.http import HttpResponse

def newyear(request):
    
    now=datetime.datetime.now()
    return render(request,"check.html",{
        "value": now.day==1 and now.month==1
    })