from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Wedding front page")

def rsvp(request):
    return HttpResponse("rsvp here")

def registry(request):
    return HttpResponse("Registry page")

def accomodations(request):
    return HttpResponse("Hotels around the area. Things to do.")
