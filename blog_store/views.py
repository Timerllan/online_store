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
        super().__init__(**kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = [
        "title",
        "content",
        "preview",
    ]
    success_url = reverse_lazy("blog_store:blogpost_list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        slug = self.kwargs.get("slug")
        return get_object_or_404(self.model, pk=pk, slug=slug)


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_store:blogpost_list")


def activity(request, pk, slug):
    blogpost = get_object_or_404(BlogPost, pk=pk, slug=slug)
    if blogpost.is_published:
        blogpost.is_published = False
    else:
        blogpost.is_published = True

    blogpost.save()

    return redirect(reverse_lazy("blog_store:blogpost_list"))
