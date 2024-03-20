## Template-Based Notification

**Email:**

* **Current Approach:** Email notification templates are currently stored locally
* **Future Enhancements:** We can consider using a database to store template related data, also can implement UI to create new templates.

**Sample payload for testing template based email:**

```
curl --location 'http://localhost:8000/notifications' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "channels": [
    "email"
  ],
  "email_req": {
    "sender": {
      "name": "Flexnest",
      "email": "no-reply@theflexnest.com"
      // Hardcoded for demo purposes. We can connect the client's domain to use their sender email addresses.
    },
    "recipients": [
      {
        "name": "Raj Malhotra",
        "email": "rajmalhotra@gmail.com"
      }
    ],
    "subject": "We've Received Your Order",
    "template_name": "order_confirmation",
    "variables": [
      {
        "var": "company_name",
        "value": "Flexnest"
      },
      {
        "var": "order_link",
        "value": "https://www.theflexnest.com/track-order?order_number=1234"
      },
      {
        "var": "order_number",
        "value": "1234"
      },
      {
        "var": "customer_name",
        "value": "Raj Malhotra"
      }
    ]
  }
}'
```

**WhatsApp:**

WhatsApp provides an API for creating message templates. However, approval for these templates may be required.

**SMS:**

Many email providers also offer SMS support. In such cases, text-based templates can be used.