from django.urls import path

from .views import main

app_name = "students_list"

urlpatterns = [
    path("", main, name="main"),
]
