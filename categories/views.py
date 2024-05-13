from django.shortcuts import render, get_object_or_404
from categories.models.product import Product


# Create your views here.


def product_store(request):
    product = Product.objects.all()
    all_product = {"product": product}
    return render(request, "catalog/product.html", all_product)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)


def contact_card(request):
    return render(request, "catalog/con_contact_card.html")
