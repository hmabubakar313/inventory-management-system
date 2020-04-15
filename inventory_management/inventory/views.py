from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def display_laptop(request):
    items=Laptops.objects.all()
    context={
        'items':items,
    }
    return render(request,'index.html',context)


def desktop(request):
    items=Desktops.objects.all()
    context={
        'items':items,
    }
    return render(request,'index.html',context)
    

def mobile(request):
    items=Mobiles.objects.all()
    context={
        'items':items,
    }
    return render(request,'index.html',context)
    