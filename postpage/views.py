from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

 
def newpost(request):

    
    return render (request, "newpost.html", {})