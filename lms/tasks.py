from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_course_update_email(course_id, subscriber_emails):
    subject = f"Course {course_id} updated!"
    message = f"The course with ID {course_id} has been updated. Check it out!"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, subscriber_emails)
    return f"Emails sent to {len(subscriber_emails)} subscribers."
