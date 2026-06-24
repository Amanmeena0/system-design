from abc import ABC, abstractmethod

class Sender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender(Sender):
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification with message: {message}")

class SMSNotificationSender(Sender):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification with message: {message}")

class NotificationService:
    def __init__(self, sender:Sender)-> None:
        self.sender = sender
    
    def send(self, message: str) -> None:
        self.sender.send_notification(message)