from typing import Dict

from mailersend import emails

from notification_handler.base import NotificationChannel
import settings


class EmailNotificationChannel(NotificationChannel):
    def __init__(self):
        self.api_key = settings.MAILERSEND_API_KEY
        self.default_sender_email = settings.DEFAULT_SENDER_EMAIL
        self.mailer = emails.NewEmail(mailersend_api_key=self.api_key)
        self.mail_body = {}

    def send_notification(self, request: Dict) -> Dict[str, str]:
        """
        Sends an email notification based on the provided request details.
        """
        email_req = request.get("email_req", {})

        try:
            mail_from = {
                "name": email_req.get("sender_name", "Test"),
                "email": self.default_sender_email,
            }
            recipients = email_req.get("recipients", [])
            subject = email_req.get("subject", "")
            html_content = email_req.get("html_content", "")
            plaintext_content = email_req.get("plaintext_content", "")

            self.mailer.set_mail_from(mail_from, self.mail_body)
            self.mailer.set_mail_to(recipients, self.mail_body)
            self.mailer.set_subject(subject, self.mail_body)
            self.mailer.set_html_content(html_content, self.mail_body)
            self.mailer.set_plaintext_content(plaintext_content, self.mail_body)

            response_string = self.mailer.send(self.mail_body)
            status_code, response_text = response_string.split("\n")

            if status_code in ["200", "201", "202"]:
                return {"message": "Email sent successfully!", "status_code": status_code, "response": response_text}
            elif status_code == "401":
                return {"message": "Unauthenticated. Please check your API credentials."}
            else:
                return {"message": f"Error sending email.", "status_code": status_code, "response": response_text}

        except Exception as e:
            return {"message": "Error sending email", "error": str(e)}
