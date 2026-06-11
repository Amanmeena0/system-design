class Vehicle:
    def __init__(self, make:str, model:str, year:int):
        self._make = make
        self._model = model
        self._year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")


class ElectricCar(Vehicle):
    def __init__(self, make:str, model:str, year:str, battery_capacity:int):
        super().__init__(make, model, year)
        self._battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"Charging {self._battery_capacity}kwh battery")


class GasCar(Vehicle):
    def __init__(self, make:str, model:str, year:str, fuel_tank_size:float):
        super().__init__(make, model, year)

    def fill_bank(self):
        print(f"Filling {self._fuel_tank_size}L fuel tank")