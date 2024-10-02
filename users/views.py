from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterUserForm
from users.models import User


class RegisterUser(CreateView):

    model = User
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
