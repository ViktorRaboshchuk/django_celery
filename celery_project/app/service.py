from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "Вы подписались на рассылку",
        "Мы будем присылать вам много писем",
        "",
        [user_email],
        fail_silently=False,
    )