from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Writing endpoints - location on webserver etc

def main(request):
    #request parameter compulsory in views
    #endpoint returns response to sender
    return HttpResponse("Hello World")
