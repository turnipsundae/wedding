from django.shortcuts import render

from django.http import HttpResponse

from .models import Meal, Guest

# Create your views here.
def index(request):
    return render(request, 'wedding/index.html')

def rsvp(request):
    return render(request, 'wedding/rsvp.html')

def registry(request):
    return render(request, 'wedding/registry.html')

def accomodations(request):
    return render(request, 'wedding/accomodations.html')
