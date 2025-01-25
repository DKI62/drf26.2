from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from users.models import CustomUser


class Command(BaseCommand):
    help = "Создает тестовых пользователей с разным временем последнего входа"

    def handle(self, *args, **kwargs):
        # Пользователь, который давно не заходил
        old_user = CustomUser.objects.create(
            email="inactive_user@example.com",
            is_active=True
        )
        old_user.last_login = now() - timedelta(days=40)
        old_user.save()

        # Пользователь, который заходил недавно
        recent_user = CustomUser.objects.create(
            email="active_user@example.com",
            is_active=True
        )
        recent_user.last_login = now() - timedelta(days=10)
        recent_user.save()

        self.stdout.write(self.style.SUCCESS("Тестовые пользователи успешно созданы!"))
