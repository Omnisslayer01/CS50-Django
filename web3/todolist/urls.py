from . import views
from django.urls import path

app_name="tasks"
urlpatterns=[
    path('tasks/',views.mylist,name="mylist"),
    path('addtasks/',views.add,name="addtasks")
]