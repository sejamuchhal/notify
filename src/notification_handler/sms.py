from typing import Dict
from notification_handler.base import NotificationChannel

class SMSNotificationChannel(NotificationChannel):
  def send_notification(self, request: Dict) -> None:
    raise NotImplementedError("SMS notification not implemented yet")