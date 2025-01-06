from django.urls import path
from django.views.decorators.cache import cache_page

from categories.apps import CategoriesConfig  # Импорт для формирования ключа

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
)

app_name = CategoriesConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_store"),  # Список продуктов
    path(
        "contact/", ProductCreateView.as_view(), name="product_form"
    ),  # Форма создания продукта
    path(
        "product_store/product_detail/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path(
        "product_store/product_update/<int:pk>/",
        ProductUpdateView.as_view(),
        name="update_forms",
    ),  # Обновление продукта
]
