# onlinequiz/apps.py

from django.apps import AppConfig
from django.conf import settings

class OnlinequizConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "onlinequiz"

    def ready(self):
        if settings.DEBUG:
            return

        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = "admin"
            email = "admin@gmail.com"
            password = "182358"

            user, _ = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": email,
                    "is_staff": True,
                    "is_superuser": True,
                },
            )

            # 🔑 FORCE password fix (critical)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()

        except Exception:
            pass
