from django.shortcuts import render

# Create your views here.
def all_products(request):
    """A view to render a list with all the products"""
    return render(request, 'products/products.html')