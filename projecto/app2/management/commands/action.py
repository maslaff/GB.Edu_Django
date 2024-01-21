from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Do something"

    def handle(self, *args, **kwargs):
        self.stdout.write("I do do dooo... Something!")
