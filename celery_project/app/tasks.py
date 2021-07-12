from django.core.mail import send_mail

from app.models import Contact
from app.service import send
from celery_project.celery import app


@app.task
def send_spam_email(user_email):
    send(user_email)


# @app.task
# def send_beat_email():
#     for contact in Contact.objects.all():
#         send_mail(
#             "Вы подписались на рассылку",
#             "Мы будем присылать вам письмо каждые 5 мин",
#             "",
#             [contact],
#             fail_silently=False,
#         )