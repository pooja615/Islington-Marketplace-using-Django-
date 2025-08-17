from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from Blogs.models import Category, Blog
from pages.models import Page

def home(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()[:3]
    pages = Page.objects.all()

    return render(request, 'home/home1.html', {
        'products': products,
        'blogs': blogs,
        'pages': pages
        })


"""
def home(request):
    products = [
        {'name': 'Laptop', 'Price': 150000},
        {'name': 'Book', 'Price': 300},
        {'name': 'Camera', 'Price': 25000},
        {'name': 'Powerbank', 'Price': 3000},
        {'name': 'Bottle', 'Price': 5000},
        {'name': 'Monitor', 'Price': 12000},
        {'name': 'Laptop Stand', 'Price': 900},
        {'name': 'Tshirt', 'Price': 2200},
    ]

    return render(request, 'home/home.html', {'products': products})
"""
    