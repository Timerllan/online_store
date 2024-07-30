from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from blog_store.models import BlogPost
from .forms import BlogForms


class BlogCreateView(CreateView):
    model = BlogPost
    success_url = reverse_lazy("blog_store:blogpost_list")
    form_class = BlogForms
    # form_valid()
    # обработка валидации формы, используется в контроллерах
    # form_valid()обработка валидации формы, используется в контроллерах
    # form_invalid()обработка невалидной формы, используется в контроллерах
    # CreateView и UpdateView


class BlogListView(ListView):
    model = BlogPost
    # get_paginate_by()
    # получение количества записей для постраничного вывода,
    # используется только в контроллере ListView.


class BlogDetailView(DetailView):
    model = BlogPost

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    # get_queryset()получение запроса для формирования данных, используется в каждом контроллере.
    # get_context_data()получение контекста для формирования ответа,
    # который будет рендериться из шаблона, используется в каждом контроллере


class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogForms
    success_url = reverse_lazy("blog_store:blogpost_list")

    # form_valid()
    # обработка валидации формы, используется в контроллерах
    # form_valid()обработка валидации формы, используется в контроллерах
    # form_invalid()обработка невалидной формы, используется в контроллерах
    # CreateView и UpdateView

    def get_object(self, queryset=None):  # получение запроса для формирования данных,
        # используется в каждом контроллере.
        pk = self.kwargs.get("pk")
        slug = self.kwargs.get("slug")
        return get_object_or_404(self.model, pk=pk, slug=slug)

    # get_queryset()получение запроса для формирования данных, используется в каждом контроллере.
    # get_context_data()получение контекста для формирования ответа,
    # который будет рендериться из шаблона, используется в каждом контроллере


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_store:blogpost_list")

    # get_queryset()получение запроса для формирования данных, используется в каждом контроллере.
    # get_context_data()получение контекста для формирования ответа,
    # который будет рендериться из шаблона, используется в каждом контроллере


def activity(request, pk, slug):
    blogpost = get_object_or_404(BlogPost, pk=pk, slug=slug)
    if blogpost.is_published:
        blogpost.is_published = False
    else:
        blogpost.is_published = True

    blogpost.save()

    return redirect(reverse_lazy("blog_store:blogpost_list"))
