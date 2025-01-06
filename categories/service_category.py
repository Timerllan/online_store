from django.core.cache import cache


from .models import Category


def get_categories():
    """
    Сервисная функция для выборки всех категорий с кешированием результата.
    """
    categories = cache.get("all_categories")
    if not categories:
        categories = list(Category.objects.all())
        cache.set("all_categories", categories, timeout=None)
    return categories
