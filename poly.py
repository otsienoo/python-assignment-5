# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # This method will be overridden in each subclass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Testing Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves in its own way
