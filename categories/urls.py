from django.urls import path

from .views import index, contact

app_name = 'students_list'

urlpatterns = [
    path('', index, name="index"),
    path("contacts/", contact, name="contact")

]
