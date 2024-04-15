from django.db import models


#Create your models here.
NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=100)  # Наименование
    description = models.TextField(max_length=150)  # Описание
    image = models.ImageField(upload_to='image_product/', name='изображение_продукта', **NULLABLE)  # Изображение
    category = models.CharField(max_length=50)  # Категория
    price_per_purchase = models.IntegerField(max_length=100)  # Цена за покупку
    date_of_creation = models.DateTimeField(auto_now_add=True)  # Дата создания (записи в БД)
    date_of_last_change = models.DateTimeField(auto_now=True)  # Дата последнего изменения (записи в БД)

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'



class Category(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
