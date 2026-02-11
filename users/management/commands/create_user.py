from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="k.ekke2906@gmail.com")
        user.set_password("1234")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
