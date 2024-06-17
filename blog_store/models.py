from django.db import models
import pytils.translit

# Create your models here.
NULLABLE = {"blank": True, "null": True}

from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="URL", unique=True)
    content = models.TextField(verbose_name="Содержание заголовка")
    preview = models.ImageField(
        upload_to="image_blog", verbose_name="Изображение", **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Активно")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Коллличество просмотров"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = pytils.translit.slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
