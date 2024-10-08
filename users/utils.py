from django.core.mail import send_mail
from itsdangerous import URLSafeTimedSerializer
from django.urls import reverse
from django.conf import settings

from users.token import generate_random_password


def send_verification_email(user):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    token = serializer.dumps(user.email, salt=settings.SECRET_KEY)
    link = reverse('users:verify_email', kwargs={'token': token})
    full_link = f"{settings.FRONTEND_URL}{link}"

    send_mail(
        subject='Подтверждение электронной почты',
        message=f'Пожалуйста, подтвердите вашу почту, перейдя по следующей ссылке: {full_link}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )




def send_password_reset_email(user):
    new_password = generate_random_password()  # Генерация нового пароля
    user.set_password(new_password)  # Установка нового пароля для пользователя
    user.save()  # Сохранение изменений в базе данных

    subject = 'Ваш новый пароль'
    message = f'Ваш новый пароль: {new_password}'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )