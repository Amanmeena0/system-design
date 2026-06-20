class LineItem:
    def __init__(self, product_name, quantity, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_subtotal(self):
        return self.quantity * self.unit_price
    def describe(self):
        print(f"Product: {self.product_name} X Quantity: {self.quantity} @ Unit Price: ${self.unit_price:.2f} = ${self.get_subtotal():.2f}")

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.line_items = []

    def add_item(self, product, quantity, unit_price):
        self.line_items.append(LineItem(product, quantity, unit_price))

    def remove_item(self, product):
        self.line_items = [
            item for item in self.line_items
            if item.product_name != product
        ]

    def get_total(self):
        return sum(item.get_subtotal() for item in self.line_items)
    

    def print_receipt(self):
        print(f"Order ID: {self.order_id}")
        print("Items:")
        for item in self.line_items:
            item.describe()
        print(f"Total: ${self.get_total():.2f}")

if __name__ == "__main__":
    order = Order("12345")
    order.add_item("Widget", 2, 10.00)
    order.add_item("Gadget", 1, 15.50)
    order.print_receipt()
    order.remove_item("Widget")
    order.print_receipt()