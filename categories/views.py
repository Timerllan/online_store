from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from categories.models.product import Product


# Create your views here.


def product_store(request):
    product = Product.objects.all()
    all_product = {"product": product}
    return render(request, "catalog/product.html", all_product)


def main_store(request):
    return render(request, "catalog/main_store.html")


def contact_card(request):
    return render(request, "catalog/con_contact_card.html")
