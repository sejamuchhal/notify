from fastapi import APIRouter, HTTPException
from app.schemas import NotificationRequest
from app.celery_worker import send_notification_task

router = APIRouter()

@router.post("/notifications")
async def send_notification(request: NotificationRequest):
    try:
        serialized_data = request.model_dump()
        task_result = send_notification_task.delay(serialized_data)
        return {"message": "Notification submitted for processing", "task_id": task_result.task_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to submit notification: {str(e)}")
