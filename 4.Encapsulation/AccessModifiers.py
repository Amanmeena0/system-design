## Access Modifiers

class Product:
    def __init__(self,name:str, price:float):
        self._name = name # Name-mangaled (private by convention)
        self._price = price # Name-mangaled (private by convention)

    def get_name(self) -> str: # Anyone can read the name
        return self._name 
    def get_pricec(self) -> float: # Anyone can read the price
        return self._price
    

