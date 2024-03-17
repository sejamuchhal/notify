from celery import Celery
from app.schemas import NotificationRequest

app = Celery('notification-worker', broker='amqp://guest:guest@rabbitmq:5672/vhost', backend='rpc://')


@app.task
def send_notification_task(request: dict):
    return {"message": "Notification processed", "request": request}