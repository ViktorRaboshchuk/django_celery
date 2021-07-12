import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_shcedule = {
#     'send-meil': {
#         'task': 'main.tasks.send_beat_email',
#         'shcedule': crontab(minute='*/5')
#     }
# }