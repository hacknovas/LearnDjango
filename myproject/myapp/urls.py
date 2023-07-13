from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("home/", view=home,name="home"),
    path("index/", view=index,name="index")
]
