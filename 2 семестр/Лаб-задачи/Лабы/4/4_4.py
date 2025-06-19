class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

class Car(Vehicle):
    def drive(self):
        print("Машина едет")

class Bike(Vehicle):
    def ride(self):
        print("Велосипед едет")

class Truck(Vehicle):
    def take(self):
        print("Грузовик едет")

car = Car(40, 50)
car.drive()

bike = Bike(10, 0)
bike.ride()

truck = Truck(30, 100)
truck.take()