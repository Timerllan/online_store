# Generated by Django 4.2.7 on 2024-09-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_current_version",
            field=models.BooleanField(
                default=False, verbose_name="Признак текущей версии"
            ),
        ),
    ]
