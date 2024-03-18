from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, validator


class EmailReq(BaseModel):
  body: str
  subject: str
  recipients: List[EmailStr]
  sender: Optional[EmailStr] = None
  html_content: Optional[str] = None

  @classmethod
  def from_dict(cls, data: Dict):
    return cls(**data)
class NotificationRequest(BaseModel):
    channels: List[str]
    email_req: Optional[EmailReq] = None

    @validator("channels")
    def validate_channels(cls, value):
        valid_channels = ["email", "sms", "whatsapp"]
        if not all(channel in valid_channels for channel in value):
            raise ValueError("Invalid channel(s). Supported channels: email, sms, whatsapp.")
        return value