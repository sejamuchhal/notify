from typing import Dict
from notification_handler.base import NotificationChannel


class WhatsAppNotificationChannel(NotificationChannel):
    def send_notification(self, request: Dict) -> None:
        raise NotImplementedError("WhatsApp notification not implemented yet")
