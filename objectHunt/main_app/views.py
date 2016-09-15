from django.shortcuts import render

#Importing class from module so that we can create appropriate http response.
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('<h1> Knowing every detail of a programming language is of paramount importance.</h1>')