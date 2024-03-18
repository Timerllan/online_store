from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "catalog/index.html")


def contact(request: WSGIRequest):
    if request.POST:
        print(request.POST)
    return render(request, "catalog/contacts.html")
