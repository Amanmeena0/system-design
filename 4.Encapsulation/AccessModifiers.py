## Access Modifiers
class Product:
    def __init__(self,name:str, price:float):
        self.__name = name # Name-mangaled (private by convention)
        self.__price = price # Name-mangaled (private by convention)

    def get_name(self) -> str: # Anyone can read the name
        return self.__name 
    def get_price(self) -> float: # Anyone can read the price
        return self.__price
    
if __name__ == "__main__":
    prod = Product("aman", 43.64)

    print(prod.get_name())
    print(prod.get_price())

# we can access the private attributes indirectly by using methods or getters/setteres. But we can't access them directly.
class Product:
    def __init__(self, name):
        self.name = name          # Public
        self._category = "Tech"   # Protected
        self.__price = 1000       # Private

p = Product("Laptop")

print(p.name)        # ✅ Works
print(p._category)   # ✅ Works (but not recommended)
print(p.__price)     # ❌ Error