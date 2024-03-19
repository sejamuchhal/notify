from celery import Celery
from celery.result import AsyncResult

import settings

def create_celery_app():
    app = Celery(
        main='__main__',
        broker_url=settings.CELERY_BROKER_URL,
        backend=settings.CELERY_RESULT_BACKEND,
    )
    app.conf.update(
        result_persistent=True,
        task_routes=settings.CELERY_TASK_ROUTES,
        task_queues=settings.CELERY_TASK_QUEUES,
    )
    return app

celery_app = create_celery_app()

def get_task_info(task_id):
    """
    Retrieves information about a Celery task given its id.
    """
    task_result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
