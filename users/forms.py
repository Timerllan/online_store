from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


