from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from blog_store.models import BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = [
        "title",
        "content",
        "preview",
    ]
    success_url = reverse_lazy("blog_store:blogpost_list")


class BlogListView(ListView):
    model = BlogPost


class BlogDetailView(DetailView):
    model = BlogPost

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
