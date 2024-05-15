from django.contrib import admin
from .models import Category
# Register your models here.


from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # список_полей_модели_для_отображения
    list_filter = ('name',)  # список_полей_для_фильтрации
    search_fields = ('name',)  # список_полей_для_поиска


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_purchase', 'category')  # список_полей_модели_для_отображения
    list_filter = ('category',)  # список_полей_для_фильтрации
    search_fields = ('name', 'description')  # список_полей_для_поиска
