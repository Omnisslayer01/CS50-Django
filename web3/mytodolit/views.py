from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

    
class newform(forms.Form):
    taskname=forms.CharField()
    priority=forms.IntegerField(min_value=1,max_value=5)

def home(request):
    if "list" not in request.session:
        request.session["list"]=[]

    return render(request,'home/home.html',{
        'tasks':request.session["list"]
    })

def add(request):
    if request.method=="POST":
        user_form=newform(request.POST)
        if user_form.is_valid():
            task=user_form.cleaned_data['taskname']
            request.session["list"]+=[task]
            return HttpResponseRedirect('/home/mytodolit')
            
        else:
            return render(request,'home/addtasks.html',{
                'myform':user_form
            })


    return render(request,'home/addtasks.html',{
        'myform':newform()
    })
    


