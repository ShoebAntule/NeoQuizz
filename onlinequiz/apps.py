from django.apps import AppConfig

class OnlinequizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlinequiz'

    def ready(self):
        from django.conf import settings
        if not settings.DEBUG:
            from django.contrib.auth.models import User
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@gmail.com',
                    password='182358'
                )
