# Notify
Notification microservice (email for now, SMS/WhatsApp planned) for event via APIs &amp; queue-based subscriptions.
> Check [docs](docs/notify.md) for detailed architecture and tech stack info.

### Prerequisites

Docker: Ensure you have Docker installed on your system.

### Running the API with Docker Compose

1. Clone this repository:
```
git clone git@github.com:sejamuchhal/notify.git
cd notify
```
2. Create a `.env` file:
```
Rename the `.example.env` file to `.env`.
Set MAILERSEND_API_KEY and DEFAULT_SENDER_EMAIL
```
2. Build and start the Docker containers:
```
docker-compose up --build
```

### Sending Notification
```
curl -X 'POST' \
  'http://localhost:8000/notifications' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "channels": [
        "email"
    ],
    "email_req": {
        "subject": "Your Flexnest Order #1234 is Out for Delivery!",
        "recipients": [
            {
                "name": "Raj",
                "email": "rajverma@gmaill.com"
            }
        ],
        "sender": {
            "name": "Flexnest Support",
            "email": "support@theflexnest.com"
        },
        "plaintext_content": "Hi Raj\nYour theflexnest order #1234 is shipped! Track it here: https://www.theflexnest.com/track-order?order_id=1234\nThanks,\n Flexnest Team\n"
    }
}'
```

### Sending email notification with attachments
```
curl --location 'http://localhost:8000/notifications/with_attachments' \
--header 'accept: application/json' \
--form 'data="{ \"channels\": [     \"email\"   ],   \"email_req\": {     \"sender\": {       \"name\": \"Flexnest Support\",       \"email\": \"support@theflexnest.com\"     },     \"recipients\": [       {         \"name\": \"Raj\",         \"email\": \"raj1234@gmail.com\"       }     ],     \"subject\": \"We'\''ve received your order\",     \"template_name\": \"order_confirmation\",      \"variables\": [       {         \"var\": \"company_name\",         \"value\": \"Flexnest\"       }, {         \"var\": \"order_link\",         \"value\": \"https://www.theflexnest.com/track-order?order_number=1234\"       }, {         \"var\": \"order_number\",         \"value\": \"1234\"       }, {         \"var\": \"customer_name\",         \"value\": \"Raj\"       }     ]   } }"' \
--form 'files=@"attachment1.txt"' \
--form 'files=@"attachment2.pdf"' \
--form 'files=@"attachment3.png"'
```

> Check [docs](docs/template_based_notification.md) for details on creating and managing template-based notifications.

## Access Flower Dashboard

The Flower dashboard provides task monitoring. Open the dashboard in browser at http://localhost:5556.


--- If you have any suggestions or encounter issues, feel free to reach out to me at sejamuchhal@gmail.com --- 