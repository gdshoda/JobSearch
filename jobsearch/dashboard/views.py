from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat",
    "february": "walk 20 mintues",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
         month_path = reverse("month_challenge", args = [month])
         list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a>/</li>"

    response_data = f"<ul>{list_items}</ul?"
    return HttpResponse(response_data)

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args = [redirect_month])
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>There's Nothing There!</h1>")
    

# def january(request):
#     return HttpResponse("This is January!")

# def february(request):
#     return HttpResponse("This is February")