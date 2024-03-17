from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator


class EmailNotification(BaseModel):
    body: str
    subject: str
    recipients: List[EmailStr]
    sender: EmailStr

class NotificationRequest(BaseModel):
    channels: List[str]
    email: Optional[EmailNotification] = None

    @validator("channels")
    def validate_channels(cls, value):
        valid_channels = ["email", "sms", "whatsapp"]
        if not all(channel in valid_channels for channel in value):
            raise ValueError("Invalid channel(s). Supported channels: email, sms, whatsapp.")
        return value