from django.shortcuts import render, get_object_or_404
from categories.models.product import Product
from django.views.generic import ListView, DetailView

# Create your views here.


class ProductListView(ListView):
    model = Product


#
class ProductDetailView(DetailView):
    model = Product


def contact_card(request):
    return render(request, "categories/con_contact_card.html")
