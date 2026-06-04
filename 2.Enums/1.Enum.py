from enum import Enum

class OrderStatus(Enum):

    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


status = OrderStatus.SHIPPED

if status == OrderStatus.SHIPPED:
    print("Your package is on the way")

class Coin(Enum):

    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self.coin_value = value
    
    def get_value(self):
        return self.coin_value
    


total = Coin.DIME.get_value() + Coin.QUARTER.get_value()

print(total)