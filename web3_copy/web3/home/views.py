from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def function(request):
   if time.strftime("%m-%d")=="12-26":
        return render(request,"home/yes_Christmas.html")
   else:
       return render(request,"home/no_Christmas.html")