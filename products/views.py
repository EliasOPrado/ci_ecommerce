from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all() #will return all objects from the # db
    return render(request, 'products.html', {'products': products})
