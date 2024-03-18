from notification_handler.base import NotificationChannel
from notification_handler.email import EmailNotificationChannel
from notification_handler.sms import SMSNotificationChannel
from notification_handler.whatsapp import WhatsAppNotificationChannel

def get_notification_handler(channel: str) -> NotificationChannel:
  if channel == "email":
    return EmailNotificationChannel()
  elif channel == "sms":
    return SMSNotificationChannel()
  elif channel == "whatsapp":
    return WhatsAppNotificationChannel()
  else:
    raise ValueError(f"Unsupported notification channel: {channel}")