from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def naruto(request):
    return HttpResponse('Naruto Uzumaki sharingan')