from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def greeting (request):
    return HttpResponse("Hello World")
def rmlau (request):
    return HttpResponse("Welcome to avadh university")
def ayodhya (request):
    return HttpResponse("Welcome to ayodhya ")