from django.urls import path 
from . import views

urlpatterns=[
    path("home/",views.function,name="app"),
    path("diyan",views.hi,name="hi"),
    path("DIO/<str:name>",views.Zawardo,name="DIO"),
    #path("<str:name>",views.greet,name="Saying Hello"),
    
]