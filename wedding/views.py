from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Meal, Guest

from django.utils.translation import ugettext_lazy as _, activate

from datetime import date

# Create your views here.
def index(request):
    WEDDING_DATE = date(2018, 1, 28)
    wedding_date = _("{day}, {month} {date}, {year}").format(
        day=WEDDING_DATE.strftime("%A"), 
        month=WEDDING_DATE.strftime("%B"), 
        # month2 is for chinese only
        month2=WEDDING_DATE.strftime("%-m"),
        # ##########################
        date=WEDDING_DATE.day, 
        year=WEDDING_DATE.year)
    context = {
        "wedding_date" : wedding_date,
    }
    return render(request, 'wedding/index.html', context)

def rsvp(request):
    if request.method == "POST":
        params = request.POST

        attending = params.get("attendingRadios", "")
        if attending == "yes":
            attending = True
        elif attending == "no":
            attending = False
        else:
            attending = None

        meal = params.get("meal", "")
        meal = get_object_or_404(Meal, choice__startswith=meal)

        guest = Guest(first_name=params.get("first_name", ""),
            last_name=params.get("last_name", ""),
            email=params.get("email", ""),
            attending=attending,
            meal=meal,
            relationship_to_wedding_party=params.get("relationshipRadios", ""),
            comments=params.get("comments", ""),
            )
        
        guest.save()

        return render(request, 'wedding/rsvp_complete.html')
    return render(request, 'wedding/rsvp.html')

def registry(request):
    return render(request, 'wedding/registry.html')

def accomodations(request):
    return render(request, 'wedding/accomodations.html')

def test(request):
    return render(request, 'wedding/test.html')
