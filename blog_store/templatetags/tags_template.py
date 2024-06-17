from categories.templatetags.tags_tags import media_filter
from django import template


register = template.Library()
register.filter("media_filter", media_filter)
