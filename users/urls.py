from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from users.apps import UsersConfig
from users.views import RegisterUser

app_name = UsersConfig.name

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
]
