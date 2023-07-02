from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myView(request):
    return HttpResponse('Hello, demo') 

def drinks(request, drink_name):
    choice_of_drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }
    return HttpResponse(f'<h2> {drink_name} </h2>{choice_of_drink[drink_name]}')

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")