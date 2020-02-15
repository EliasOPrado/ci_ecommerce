from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A view that render the cart contents page """
    return render(request, 'cart.html')

def add_to_cart(request):
    """Add a quantity of specific product to the cart """
    quantity = int(request.post.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('index'))

def adjust_cart(request, id):
    """Adjust the quantity of a specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
