from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country", "password1", "password2")
