from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, validator

class EmailRecipient(BaseModel):
    name: str
    email: EmailStr

class EmailReq(BaseModel):
  sender: Optional[EmailRecipient] = None
  recipients: List[EmailRecipient]
  subject: str
  plaintext_content: Optional[str] = None
  html_content: Optional[str] = None

class NotificationRequest(BaseModel):
    channels: List[str]
    email_req: Optional[EmailReq] = None

    @validator("channels")
    def validate_channels(cls, value):
        valid_channels = ["email", "sms", "whatsapp"]
        if not all(channel in valid_channels for channel in value):
            raise ValueError("Invalid channel(s). Supported channels: email, sms, whatsapp.")
        return value