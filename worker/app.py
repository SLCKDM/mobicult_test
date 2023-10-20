from celery import Celery
from celery.schedules import crontab

tasks = [
    'worker.tasks',
]

app = Celery('celery_worker', include=tasks)
app.config_from_object('worker.config')

app.conf.beat_schedule = {
    'every': {
        'task': 'worker.tasks.load_current_xchange_rate',
        'schedule': crontab(minute='*/1'),
    }
}

if __name__ == '__main__':
    app.start()
