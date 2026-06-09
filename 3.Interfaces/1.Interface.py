from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass

class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Stripe: ${amount}")

class RajorpayPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Razorpay: Rupees{amount}")

class CheckoutService:
    def __init__(self,payment_gateway):
        self.payment_gateway = payment_gateway

    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)

if __name__ == "__main__":
    strip_gateway = StripePayment()
    checkout_service = CheckoutService(strip_gateway)
    checkout_service.checkout(120.50) # Output: Processing payment via stripe: $120.5

    razorpay_gateway = RajorpayPayment()
    checkout_service.set_payment_gateway(razorpay_gateway)
    checkout_service.checkout(150.50) # Output: Processing payment via Razorpay: ruppees 150.5
