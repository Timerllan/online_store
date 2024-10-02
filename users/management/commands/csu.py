from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="sergeevp284@gmail.com",
            phone="89964439402",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("12345")
        user.save()
