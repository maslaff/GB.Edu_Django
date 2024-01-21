from django.core.management.base import BaseCommand
from app2.models import User


class Command(BaseCommand):
    help = "Create User."

    def handle(self, *args, **kwargs):
        # user = User(name="Ivan", age=30, email="ivan@post.ru", password="******")
        # user = User(name="Oleg", age=30, email="oleg@post.ru", password="******")
        user = User(
            name="Jaroslav", age=30, email="jaroslav@post.ru", password="******"
        )

        user.save()
        self.stdout.write(f"{user}")
