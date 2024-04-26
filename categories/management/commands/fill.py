from django.core.management import BaseCommand
from categories.models import Product, Category
import json
import datetime


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('categories/fixtures/category.json', 'r', encoding='utf-8') as file:
            c = json.load(file)
            return c

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open('categories/fixtures/product.json', 'r', encoding='utf-8') as file:
            p = json.load(file)
            return p

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()
        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            category_name = product['fields']['category']
            category, _ = Category.objects.get_or_create(name=category_name)

            product_obj = Product(
                name=product['fields']['name'],
                description=product['fields']['description'],
                category=category,
                price_per_purchase=product['fields']['price_per_purchase'],
                date_of_creation=datetime.datetime.strptime(product['fields']['date_of_creation'],
                                                            "%Y-%m-%dT%H:%M:%S.%fZ"),
                date_of_last_change=datetime.datetime.strptime(product['fields']['date_of_last_change'],
                                                               "%Y-%m-%dT%H:%M:%S.%fZ"),
                manufactured_at=datetime.datetime.strptime(product['fields']['manufactured_at'], "%Y-%m-%d")
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
