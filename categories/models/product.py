from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {"blank": True, "null": True}  # делает не обязательным
# заполнения поля
# если не заполнить
# то оно является обязательным для заполнения


# формирует в бд таблицы
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")  # Наименование
    description = models.TextField(verbose_name="Описание")  # Описание
    image_product = models.ImageField(
        verbose_name="Изображение товара",
        upload_to="image_product/",
        name="image_product",
        **NULLABLE
    )  # Изображение

    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категории спорта"
    )  # Категория здесь идёт связь
    # таблиц
    # Продуктов и категории
    price_per_purchase = models.IntegerField(
        verbose_name="Устанока цены"
    )  # Цена за покупку
    date_of_creation = models.DateTimeField(
        auto_now_add=True
    )  # Дата создания (записи в БД)
    date_of_last_change = models.DateTimeField(
        auto_now=True
    )  # Дата последнего изменения (записи в БД)
    # manufactured_at = models.DateField()  # Дата производства продукта

    author = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    is_published = models.BooleanField(
        default=False, verbose_name="признак публиукации"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        permissions = [
            ("can_change_product_categories", "Может изменять название Категории"),
            ("can_set_product_published", "Может изменять статус публикации"),
            ("can_change_description", "может менять описание любого продукта"),
        ]
