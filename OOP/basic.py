class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are mean of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


car = Car("Toyota", "Corolla")
print(car.full_name())
print(car.get_brand())
print(car.fuel_type())

my_tesla = ElectricCar("tesla", "Model s", "85KWh")
print(my_tesla.full_name())
print(my_tesla.fuel_type())

print(Car.total_car)
print(Car.general_description())
print(car.model)

print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))
