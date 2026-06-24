class SeatValidator():
    def isSeatAvailable(self, eventId, seatNumber) -> bool:
        print(f"Checking seat {seatNumber} for event {eventId}")
        return True
    
class PaymentProcessor():
    def charge(self, email, amount) -> bool:
        print(f"Charging ${amount} to {email}")
        return True
    
class QRCodeGenerator():
    def generate(self, eventId, seatNumber) -> str:
        qr_code = f"QR-{eventId}-{seatNumber}"
        print(f"Generated QR code: {qr_code}")
        return qr_code

class EmailService():
    def sendConfirmation(self, email, qrCode):
        print(f"Sending confirmation to {email} with the {qrCode}")

class TicketBookingService():
    def book_ticket(self, eventID, seatNumber, email, amount, validator, payment, qr_generator, email_service):
        if validator.isSeatAvailable(eventID, seatNumber):
            print("Seat not available")
            return False
        if not payment.charge(email, amount):
            print("Payment Failed")
            return False
        
        qr_code = qr_generator.generate(eventID, seatNumber)
        email_service.send_confirmation(email, qr_code)

        print("Booking Confirmed")
        return True
    
if __name__ == "__main__":
    booking_service = TicketBookingService()

    # All dependencies are created externally and passed in
    validator = SeatValidator()
    payment = PaymentProcessor()
    qr_generator = QRCodeGenerator()
    email_service = EmailService()

    booking_service.book_ticket("CONF-2025", "A12", "alice@example.com", 99.99, validator, payment, qr_generator, email_service)		