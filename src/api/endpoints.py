from fastapi import APIRouter, HTTPException

from api.schemas import NotificationRequest
from worker.celery_config import get_task_info
from worker.tasks import send_notification_task

router = APIRouter()


@router.post("/notifications")
async def send_notification(request: NotificationRequest):
    """
    Submits a notification for asynchronous processing.
    """
    try:
        serialized_data = request.model_dump()
        task_result = send_notification_task.apply_async(args=[serialized_data])
        return {
            "message": "Notification submitted for processing",
            "task_id": task_result.task_id,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to submit notification: {str(e)}"
        )


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Retrieves the status of a submitted celery task.
    """
    return get_task_info(task_id)
