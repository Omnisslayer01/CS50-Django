from . import views
from django.urls import path

urlpatterns=[
    path('mytodolit/',views.home),
    path('addtasks/',views.add,name='thisisaddtask'),
]