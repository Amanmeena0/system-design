
class Notification:
    def __init__(self, message:str, recipient:str):
        self._message = message
        self._recipient = recipient

    def send(self):
        print(f"Sending generic notification to {self._recipient}.")

class EmailNotification(Notification):
    def __init__(self, message:str, recipient:str, subject:str):
        super().__init__(message, recipient)
        self._subject = subject

    def send(self):
        print(f"Sending email to {self._recipient} with subject '{self._subject}'.")

class SMSNotification(Notification):
    def __init__(self, message:str, recipient:str, phone_number:str):
        super().__init__(message, recipient)
        self._phone_number = phone_number

    def send(self):
        print(f"Sending SMS to {self._recipient} at {self._phone_number}.")

class PushNotification(Notification):
    def __init__(self, message:str, recipient:str, device_id:str):
        super().__init__(message, recipient)
        self._device_id = device_id

    def send(self):
        print(f"Sending push notification to {self._recipient} on device {self._device_id}.")


if __name__ == "__main__":
    notifications = [
        EmailNotification("Hello, you have a new message!", "Alice", "New Message"),
        SMSNotification("Your order has been shipped!", "Bob", "+1234567890"),
        PushNotification("You have a new friend request!", "Charlie", "device123")
    ]
    for notification in notifications:
        notification.send()