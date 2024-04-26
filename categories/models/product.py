from django.db import models


# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(max_length=100)  # Наименование
    description = models.TextField()  # Описание
    image = models.ImageField(
        upload_to="image_product/", name="image_product", **NULLABLE
    )  # Изображение

    category = models.ForeignKey("Category", on_delete=models.CASCADE)  # Категория
    price_per_purchase = models.IntegerField()  # Цена за покупку
    date_of_creation = models.DateTimeField(
        auto_now_add=True
    )  # Дата создания (записи в БД)
    date_of_last_change = models.DateTimeField(
        auto_now=True
    )  # Дата последнего изменения (записи в БД)
    manufactured_at = models.DateField()  # Дата производства продукта

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
