from django.apps import AppConfig
from django.db.utils import OperationalError

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        from .models import Role
        try:
            if not Role.objects.exists():
                Role.objects.create(name="Admin")
                Role.objects.create(name="Vendor")
                Role.objects.create(name="Customer")
        except OperationalError:
            pass

