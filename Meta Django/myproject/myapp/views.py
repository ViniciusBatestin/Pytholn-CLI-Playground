from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import path
# from . import views


# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon restaurant! </h1")
