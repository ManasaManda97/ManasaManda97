from .cart import Cart  #importing cart class from cart.py


def cart(request):
    
    return {'cart': Cart(request)}