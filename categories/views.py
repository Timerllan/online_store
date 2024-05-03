from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from categories.models.product import Product
from django.http import HttpResponse

# Create your views here.


def product_store(request):
    product = Product.objects.all()
    all_product = {"product": product}
    return render(request, "catalog/product.html", all_product)


def main_store(request):
    b = {"s": "user"}
    return render(request, "catalog/main_store.html", b)
