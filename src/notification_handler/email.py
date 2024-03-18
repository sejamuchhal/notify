from typing import Dict, List, Union

from mailersend import emails

from notification_handler.base import NotificationChannel
import settings


class EmailNotificationChannel(NotificationChannel):
  def __init__(self):

    self.default_mail_from = settings.DEFAULT_SENDER_EMAIL
    self.mailer = emails.NewEmail(settings.MAILERSEND_API_KEY)
    self.mail_body = {}

  def send_notification(self, request: Dict) -> Dict[str, str]:
    """
    Sends an email notification based on the provided request details.
    """
    email_req = request.email_req

    try:
      self.mail_from = {
          "name": email_req.get("sender_name", "Test"),
          "email": self.default_mail_from
      }
      self.recipients = email_req.get("recipients", [])
      self.subject = email_req.get("subject", "")
      self.html_content = email_req.get("html_content", "")
      self.plaintext_content = email_req.get("plaintext_content", "")

      self.mailer.set_mail_from(self.mail_from, self.mail_body)
      self.mailer.set_mail_to(self.recipients, self.mail_body)
      self.mailer.set_subject(self.subject, self.mail_body)
      self.mailer.set_html_content(self.html_content, self.mail_body)
      self.mailer.set_plaintext_content(self.plaintext_content, self.mail_body)

      mail_response = self.mailer.send(self.mail_body)
      return {"message": "Email sent successfully", "mail_response": mail_response}
    except Exception as e:
      return {"message": "Error sending email", "error": str(e)}
