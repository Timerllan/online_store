from django.shortcuts import render, get_object_or_404
from categories.models.product import Product
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from categories.forms import ProductForm

# Create your views here.


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("categories:product_store")


#
class ProductDetailView(DetailView):
    model = Product
