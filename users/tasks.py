from datetime import timedelta
from django.utils.timezone import now
from celery import shared_task
from users.models import CustomUser


@shared_task
def deactivate_inactive_users():
    """
    Деактивирует пользователей, которые не заходили в систему более 30 дней.
    """
    cutoff_date = now() - timedelta(days=30)
    inactive_users = CustomUser.objects.filter(last_login__lt=cutoff_date, is_active=True)
    count = inactive_users.update(is_active=False)
    return f"Deactivated {count} inactive users."
