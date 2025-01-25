from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_course_update_email(course_title, subscribers):
    """
    Отправка уведомлений о новом обновлении курса
    """
    subject = f"Обновление курса: {course_title}"
    message = f"В курсе '{course_title}' появились новые материалы! Проверьте обновления на сайте."
    from_email = "your@yandex.ru"

    for subscriber in subscribers:
        send_mail(subject, message, from_email, [subscriber])
    return f"Emails sent to {len(subscribers)} subscribers"
