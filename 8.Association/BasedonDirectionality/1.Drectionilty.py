class PaymentGateway:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")
class order:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        self.payment_gateway.process_payment(amount)

if __name__ == "__main__":
    # Example usage
    class StripePaymentGateway(PaymentGateway):
        def process_payment(self, amount):
            print(f"Processing payment of ${amount} through Stripe.")

    stripe_gateway = StripePaymentGateway()
    order_instance = order(stripe_gateway)
    order_instance.checkout(100)