from django.urls import path
from categories.apps import CategoriesConfig  # этот иморт нужен для формирования

# {%url 'имя_приложения: имя функции'%} и.т.д
# оно формирует ключ чтоб переходить по значениям то есть по названию функции
from .views import ProductListView, ProductDetailView, contact_card

app_name = CategoriesConfig.name

urlpatterns = [
    path(
        "", ProductListView.as_view(), name="product_store"
    ),  # name - именнование функции для вызова в
    path("contact", contact_card, name="contact_card"),
    path(
        "product_store/product_detail/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
]
