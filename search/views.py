from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    # 'q' is the name="q" into the form to show the searched keyword
    products = Product.objects.filter(name__icontains=request.GET('q'))
    return render(request, "products.html", {'products': products})
