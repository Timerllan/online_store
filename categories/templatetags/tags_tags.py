from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return path.url
    return static("zaglushka.jpg")
