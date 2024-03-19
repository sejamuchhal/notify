from celery import Celery

app = Celery(
    'notification-worker',
    broker='amqp://guest:guest@rabbitmq:5672/vhost',
    backend='rpc://',
    broker_connection_retry=True,
    broker_connection_retry_on_startup=True,
)