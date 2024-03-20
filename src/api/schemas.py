from typing import List, Optional

from pydantic import BaseModel, EmailStr, root_validator, validator

from template_data_simulator import get_template_variables


class EmailRecipient(BaseModel):
    name: str
    email: EmailStr


class EmailVariable(BaseModel):
    var: str
    value: str


class EmailReq(BaseModel):
    sender: Optional[EmailRecipient] = None
    recipients: List[EmailRecipient]
    subject: str
    plaintext_content: Optional[str] = None
    html_content: Optional[str] = None
    template_name: Optional[str] = None
    variables: Optional[List[EmailVariable]] = None

    @root_validator(pre=True)
    def validate_content_or_template(cls, values):
        if not any(
            value is not None
            for value in [
                values.get("html_content"),
                values.get("plaintext_content"),
                values.get("template_name"),
            ]
        ):
            raise ValueError(
                "You must provide one of html_content, plaintext_content, or template_name."
            )
        return values

    @validator("recipients")
    def validate_recipients(cls, value):
        if not value:
            raise ValueError("At least one recipient must be specified.")
        return value

    @validator("variables")
    def validate_variables(cls, value, values):
        if value:
            if values.get("template_name"):
                required_variables = get_template_variables(values["template_name"])
                provided_variables = {variable.var for variable in value}
                missing_variables = set(required_variables) - provided_variables
                if missing_variables:
                    raise ValueError(
                        f"Missing required temp variables: {', '.join(missing_variables)}"
                    )
        return value


class NotificationRequest(BaseModel):
    channels: List[str]
    email_req: Optional[EmailReq] = None

    @validator("channels")
    def validate_channels(cls, value):
        valid_channels = ["email", "sms", "whatsapp"]
        if not all(channel in valid_channels for channel in value):
            raise ValueError(
                "Invalid channel(s). Supported channels: email, sms, whatsapp."
            )
        return value
