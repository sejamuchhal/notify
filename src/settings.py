import os
from kombu import Queue

CELERY_TASK_QUEUES = (
    Queue('default', routing_key='default'),
    Queue('notification', routing_key='notification'),
)
CELERY_TASK_ROUTES = {
    'send_notification_task': {
        'queue': 'notification',
        'routing_key': 'notification',
    },
}
CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672/vhost")
CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")

MAILERSEND_API_KEY = os.getenv("MAILERSEND_API_KEY")
DEFAULT_SENDER_NAME = os.getenv("DEFAULT_SENDER_NAME")
DEFAULT_SENDER_EMAIL = os.getenv("DEFAULT_SENDER_EMAIL")