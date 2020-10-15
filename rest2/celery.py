import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest2.settings')

app = Celery('rest2')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# Second way to beat schedule

# app.conf.beat_schedule = {
#     'add-every-5-seconds': {
#         'task': 'api.tasks.send_email',
#         'schedule': 1.0,
#         'args': ('pjkostrzewski@gmail.com', 'This is sample message.')
#     }
# }

app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')