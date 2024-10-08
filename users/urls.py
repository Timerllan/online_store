from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetDoneView, PasswordResetConfirmView
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterUser, VerifyEmailView, password_reset_view

app_name = UsersConfig.name





urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path('verify_email/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('email_verified/', TemplateView.as_view(template_name='users/email_verified.html'), name='email_verified'),
    path('invalid_token/', TemplateView.as_view(template_name='users/invalid_token.html'), name='invalid_token'),
    path('register/message_post/', TemplateView.as_view(template_name='users/message_post.html'), name='message_post'),
    path('login/password_reset/', password_reset_view, name='password_reset')
]