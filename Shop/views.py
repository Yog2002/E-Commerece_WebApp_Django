from django.shortcuts import render
from django.http import HttpResponse #Created Manually


# Create your views here.

def index(request):
    return render(request,"Shop/index.html")

def about(request):
    return HttpResponse("We Are At AboutUs")

def contact(request):
    return HttpResponse("We Are At ContactUs")

def tracker(request):
    return HttpResponse("We Are At Tracker")

def search(request):
    return HttpResponse("We Are At Search")

def proudView(request):
   return HttpResponse("We Are At ProductView")

def checkout(request):
    return HttpResponse("We Are At Checkout")
