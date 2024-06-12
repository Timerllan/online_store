from django.urls import path
from blog_store.views import BlogCreateView, BlogListView, BlogDetailView

app_name = "blog_store"

urlpatterns = [
    path("blog_create", BlogCreateView.as_view(), name="blogpost_form"),
    path("blogs", BlogListView.as_view(), name="blogpost_list"),
    path("blogs/<slug:slug>", BlogDetailView.as_view(), name="blogpost_detail"),
]


# другие urlpatterns
