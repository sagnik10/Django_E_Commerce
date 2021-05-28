from django.shortcuts import render
from django.contrib.auth import logout
from .models import Product,Laptops,Mens,Womens,Furnitures

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'index.html')


def logout(request):
    logout(request)


def main_page(request):
    objects = Product.objects.all()
    laptops = Laptops.objects.all()
    mens = Mens.objects.all()
    womens = Womens.objects.all()
    furnitures = Furnitures.objects.all()
    context = {
        'laptops' : laptops,
        'item' : objects,
        'mens' : mens,
        'womens' : womens,
        'furnitures' : furnitures
    }
    return render(request,'main_page.html',context)

def details_page(request,id):
    phone = Product.objects.filter(id=id)
    context = {
        'phone' : phone,
    }
    return render (request,'phones_details.html',context)

def laptops_details_page(request,id):
    laptops = Laptops.objects.filter(id=id)
    context = {
        'laptops' : laptops,
    }
    return render (request,'laptops_details_page.html',context)

def mens_details_page(request,id):
    mens = Mens.objects.filter(id=id)
    context = {
        'mens' : mens,
    }
    return render (request,'mens_details_page.html',context)

def womens_details_page(request,id):
    womens = Womens.objects.filter(id=id)
    context = {
        'womens' : womens,
    }
    return render (request,'womens_details_page.html',context)

def furnitures_details_page(request,id):
    furnitures = Furnitures.objects.filter(id=id)
    context = {
        'furnitures' : furnitures,
    }
    return render (request,'furnitures_details_page.html',context)

def checkout_page(request):
    return render(request,'checkout.html')