from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import category, product

# Create your views here.


def main(request):
    all_product = {"product": product}
    return render(request, "catalog/base.html", all_product)
