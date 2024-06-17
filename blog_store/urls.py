from django.urls import path
from blog_store.views import (
    BlogCreateView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    activity,
)

app_name = "blog_store"

urlpatterns = [
    path("blog_create", BlogCreateView.as_view(), name="blogpost_form"),
    path("blogs", BlogListView.as_view(), name="blogpost_list"),
    path(
        "blogs/<int:pk>-<slug:slug>", BlogDetailView.as_view(), name="blogpost_detail"
    ),
    path(
        "blog_update/<int:pk>-<slug:slug>",
        BlogUpdateView.as_view(),
        name="blogpost_form",
    ),
    path(
        "delete_blog/<int:pk>-<slug:slug>",
        BlogDeleteView.as_view(),
        name="blogpost_delete",
    ),
    path("blogs/activity/<int:pk>-<slug:slug>", activity, name="blogpost_activity"),
]


# другие urlpatterns
