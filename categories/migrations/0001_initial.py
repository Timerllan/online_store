# Generated by Django 4.2.7 on 2024-07-31 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "image_product",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="image_product/",
                        verbose_name="Изображение товара",
                    ),
                ),
                (
                    "price_per_purchase",
                    models.IntegerField(verbose_name="Устанока цены"),
                ),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
                ("date_of_last_change", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.category",
                        verbose_name="Категории спорта",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number_version",
                    models.CharField(max_length=100, verbose_name="номер версии"),
                ),
                (
                    "name_version",
                    models.CharField(max_length=100, verbose_name="название версии"),
                ),
                (
                    "is_current_version",
                    models.BooleanField(
                        default=True, verbose_name="Признак текущей версии"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия продукта",
                "verbose_name_plural": "версии продуктов",
            },
        ),
    ]
