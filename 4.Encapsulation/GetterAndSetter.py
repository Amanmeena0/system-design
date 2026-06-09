# Getter/Setter
class Product:
    def __init__(self, name:str, price:float):
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def price(self) -> str:
        return self.__price
    
    @price.setter
    def price(self, value:float)->None:
        if value < 0:
            return ValueError("Price cannot be negative.")
        self.__price = value

if __name__ == "__main__":

    prod = Product("aman", 45.323)

    print(prod.price) # Getter

    prod.price = 70.00 # Setter
    
    print(prod.price)