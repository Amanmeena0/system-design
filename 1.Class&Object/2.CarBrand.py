class Car:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._speed = 0

    def accelerate(self, increment:int):
        self._speed += increment

    def displayStatus(self):
        print(f"{self._brand} {self._model} is running at {self._speed} km/h")
    

if __name__ == "__main__":

    my_car1 = Car("Toytota", "Corolla")
    my_car2 = Car("Ford", "Mustang")

    my_car1.accelerate(100)
    my_car2.accelerate(125)

    my_car1.displayStatus()
    print("-----------------------")
    my_car2.displayStatus()
