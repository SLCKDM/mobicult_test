from celery import Celery
from celery.schedules import crontab


app = Celery('celery_worker')
app.config_from_object('worker.config')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': '<name_of_app>.tasks.repeat_order_make',
        'schedule': crontab(hour='*/24'),
    }
}
