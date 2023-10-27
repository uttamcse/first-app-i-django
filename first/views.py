from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def aim (request):
    return render(request,"index.html")



