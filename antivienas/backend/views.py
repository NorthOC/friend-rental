from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    template = "pages/index.html"
    return render(request, template)

def register(request):
    pass

def login(request):
    pass

def profile(request):
    pass

def order_manager(request):
    pass