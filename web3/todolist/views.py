from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.shortcuts import redirect




class myform(forms.Form):
    tasks=forms.CharField(max_length=100, label="New Tasks")
    Priority=forms.IntegerField(min_value=0,max_value=10)

def mylist(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request,"html/mytodolist.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method=="POST":
        submitted_form=myform(request.POST)
        if submitted_form.is_valid():
            task=submitted_form.cleaned_data["tasks"]
            request.session["tasks"]+=[task]
            #return redirect("tasks:mylist")
            return HttpResponseRedirect(reverse("tasks:mylist"))
            #return HttpResponseRedirect("/ToDoList/tasks")
        else:
            return render(request,"html/add.html",{
                "myform":submitted_form
            })
        
    return render(request,"html/add.html",{
        'myform':myform()
    })

