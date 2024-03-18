# Set RabbitMQ management api
broker_api = 'amqp://guest:guest@rabbitmq:5672/vhost'

# Enable debug logging
logging = 'DEBUG'

from flower.utils.template import humanize

def format_task(task):
    task.args = humanize(task.args)
    task.result = humanize(task.result)
    return task