from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sasuke(request):
    return HttpResponse('<marquee><h1>sasuke chidori</h1></marquee>')