from django.urls import path
from categories.apps import CategoriesConfig  # этот иморт нужен для формирования

# {%url 'имя_приложения: имя функции'%} и.т.д
# оно формирует ключ чтоб переходить по значениям то есть по названию функции
from .views import product_store, main_store

app_name = CategoriesConfig.name

urlpatterns = [
    path("product_store", product_store, name="product_store"),#name - именнование функции
    path("", main_store, name="main_store"),
]
