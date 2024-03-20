import base64
import uuid

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

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


@router.post("/notifications/with_attachments")
async def send_notification_with_attachments(
    data: str = Form("{}"), files: list[UploadFile] = File(...)
):
    """
    Submits a notification for asynchronous processing, including attachments.
    """
    try:
        notification_request = NotificationRequest.parse_raw(data)

        attachments = []
        for file in files:
            attachment_id = str(uuid.uuid4())
            file_content = file.file.read()
            att_base64 = base64.b64encode(file_content).decode("ascii")
            attachments.append(
                {
                    "id": attachment_id,
                    "filename": file.filename,
                    "content": att_base64,
                    "disposition": "attachment",
                }
            )
        notification_request.attachments = attachments
        serialized_data = notification_request.model_dump()
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
