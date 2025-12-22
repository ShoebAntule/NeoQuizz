from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create superuser if it does not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="shoebantule18@gmail.com",
                password="182358"
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists.'))
