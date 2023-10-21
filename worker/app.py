from celery import Celery
from celery.schedules import crontab

tasks = [
    'worker.tasks',
]

app = Celery('celery_worker', include=tasks)
app.config_from_object('worker.config')

app.conf.beat_schedule = {
    'EUR_RUB_xchange_rate': {
        'task': 'worker.tasks.load_current_xchange_rate',
        'schedule': crontab(hour='*/24'),
        'args': ('EUR', ('RUB',)),
    },
    'USD_RUB_xchange_rate': {
        'task': 'worker.tasks.load_current_xchange_rate',
        'schedule': crontab(hour='*/24'),
        'args': ('USD', ('RUB',)),
    },
}

if __name__ == '__main__':
    app.start()
