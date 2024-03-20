from typing import Dict, Union

from notification_handler.factory import get_notification_handler

from celery import shared_task


@shared_task(name="send_notification_task")
def send_notification_task(request: Dict) -> Dict[str, Union[str, Dict]]:
    channels = request.get("channels", [])
    responses = {}
    for channel in channels:
        notification_handler = get_notification_handler(channel)
        try:
            response = notification_handler.send_notification(request)
            responses[channel] = response
        except Exception as e:
            responses[channel] = (
                f"Error sending notification for channel {channel}: {str(e)}"
            )
    return {"message": "Notification processed", "responses": responses}
