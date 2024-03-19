from starlette.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_send_notification_valid_email():

    data = {
        "channels": ["email"],
        "email": {
            "body": "This is a test notification",
            "subject": "Test Notification",
            "recipients": ["user@example.com"],
            "sender": "sender@example.com",
        },
    }

    response = client.post("/notifications", json=data)

    assert response.status_code == 200