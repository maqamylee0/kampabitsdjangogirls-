from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello welcome to our home")

def about(request):
    return HttpResponse("we serve")    