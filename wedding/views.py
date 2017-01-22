from django.shortcuts import render

from django.http import HttpResponse

from .models import Meal, Guest

# Create your views here.
def index(request):
    return render(request, 'wedding/index.html')

def rsvp(request):
    if request.method == "POST":
        params = request.POST

        attending = params.get("attendingRadios", None)
        if attending and attending == "yes":
            attending = True
        elif attending and attending == "no":
            attending = False

        meal = params.get("meal", "chicken")
        meal = Meal.objects.filter(choice__startswith=meal).get()

        guest = Guest(first_name=params.get("first_name", ""),
            last_name=params.get("last_name", ""),
            email=params.get("email", ""),
            # attending=params.get("attending", ""),
            attending=attending,
            meal=meal,
            relationship_to_wedding_party=params.get("relationshipRadios", ""),
            comments=params.get("comments", ""),
            )
        
        # print (params.dict())

        guest.save()

        return HttpResponse("Horray Check the Console")
    return render(request, 'wedding/rsvp.html')

# def sign_up(request):
#   if request.method == "POST":
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     username = request.POST['username']
#     email = request.POST['email']
#     password = request.POST['password']
#     error_exists = False
#     params = dict(first_name=first_name, last_name=last_name, email=email)

#     if not valid_name(first_name) or not valid_name(last_name):
#       error_exists = True
#       params['error_name'] = "Enter a first and last name using only letters, apostrophes and hyphens"
#     if not valid_username(username):
#       error_exists = True
#       params['error_username'] = "Enter a username using only letters, numbers, underscore and hyphens"
#     if not valid_email(email):
#       error_exists = True
#       params['error_email'] = "Please enter in the format example@domain.com"
#     if not valid_password(password):
#       error_exists = True
#       params['error_password'] = "Minimum password length is 6 characters"
#     if error_exists:
#       return render(request, "workouts/sign_up.html", params)

#     user = User(first_name = first_name,
#                 last_name = last_name,
#                 email = email,
#                 username = username)
#     user.set_password(password)
#     user.save()
#     # TODO add sign up success message to login
#     return HttpResponseRedirect(reverse("workouts:login"))
#   else:
#     return render(request, "workouts/sign_up.html")


def registry(request):
    return render(request, 'wedding/registry.html')

def accomodations(request):
    return render(request, 'wedding/accomodations.html')

def test(request):
    return render(request, 'wedding/test.html')
