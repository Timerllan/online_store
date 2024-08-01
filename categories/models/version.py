from django.db import models


class Version(models.Model):

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    number_version = models.CharField(max_length=100, verbose_name="номер версии")
    name_version = models.CharField(max_length=100, verbose_name="название версии")
    is_current_version = models.BooleanField(
        default=False, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.name_version}, {self.number_version}"

    class Meta:
        verbose_name = "версия продукта"
        verbose_name_plural = "версии продуктов"
