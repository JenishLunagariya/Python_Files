from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("You are in About page")

def contact(request):
    return HttpResponse("You are in Contact page")

def tracker(request):
    return HttpResponse("You are in Tracker page")

def search(request):
    return HttpResponse("You are in Search page")

def prodView(request):
    return HttpResponse("You are in Productview page")

def checkout(request):
    return HttpResponse("You are in Checkout page")