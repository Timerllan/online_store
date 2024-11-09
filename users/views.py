from django.urls import reverse_lazy
from django.views.generic import CreateView
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from .utils import send_verification_email, send_password_reset_email
from .forms import RegisterUserForm
from .models import User
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:message_post')  # Укажите URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        user = form.save()
        send_verification_email(user)
        messages.success(self.request, "Пожалуйста, проверьте свою почту для подтверждения.")
        return super().form_valid(form)


class VerifyEmailView(View):

    def get(self, request, token):
        serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
        try:
            email = serializer.loads(token, salt=settings.SECRET_KEY, max_age=3600)  # 1 час
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            messages.success(request, "Ваш адрес электронной почты был успешно подтвержден.")
            return redirect('users:email_verified')  # Перенаправление на страницу подтверждения
        except (BadSignature, SignatureExpired):
            messages.error(request, "Ссылка для подтверждения недействительна или истекла.")
            return redirect('users:invalid_token')
        except User.DoesNotExist:
            messages.error(request, "Пользователь не найден.")
            return redirect('users:invalid_token')


def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            send_password_reset_email(user)
            messages.success(request, "Проверьте вашу почту для получения инструкций по сбросу пароля.")
            return redirect('users:message_post')  # Перенаправление на страницу успеха
        except User.DoesNotExist:
            messages.error(request, "Пользователь с таким адресом электронной почты не найден.")

    return render(request, 'users/password_reset.html')

