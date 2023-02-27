from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    # print("products",n)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # print("nSlides",nSlides)
    params = {'product':products,'no_of_slides':nSlides, 'range':range(1,nSlides)}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

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