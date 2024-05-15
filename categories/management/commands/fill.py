from django.core.management import BaseCommand
from categories.models import Product, Category
import json
import datetime


# данная команда создана для создания фикстуры
class Command(BaseCommand):

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open("categories/fixtures/product.json", "r", encoding="utf-8") as file:
            p = json.load(file)
            return p

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()
        # Создайте списки для хранения объектов
        all_object = Command.json_read_products()
        product_for_create = [
            Product(
                pk=product["pk"],
                name=product["fields"]["name"],
                description=product["fields"]["description"],
                category_id=product["fields"]["category"],
                price_per_purchase=product["fields"]["price_per_purchase"],
                date_of_creation=datetime.datetime.strptime(
                    product["fields"]["date_of_creation"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                date_of_last_change=datetime.datetime.strptime(
                    product["fields"]["date_of_last_change"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                manufactured_at=datetime.datetime.strptime(
                    product["fields"]["manufactured_at"], "%Y-%m-%d"
                ),
            )
            for product in all_object
            if product["model"] == "categories.product"
        ]

        category_for_create = [
            Category(
                pk=category["pk"],
                name=category["fields"]["name"],
                description=category["fields"]["description"],
            )
            for category in all_object
            if category["model"] == "categories.category"
        ]

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте

        Product.objects.bulk_create(product_for_create)
