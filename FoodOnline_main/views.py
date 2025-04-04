from django.shortcuts import render, redirect
from django.http import HttpResponse    

def home(request):
    return HttpResponse("Hello World, this is the home page!")  