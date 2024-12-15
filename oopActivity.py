# Parent Class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    # Method to be overridden in subclasses
    def move(self):
        pass

# Child Class: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗.")

# Child Class: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️.")

# Child Class: Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing 🚢.")

# Child Class: Train
class Train(Vehicle):
    def move(self):
        print(f"{self.name} is rolling on tracks 🚆.")

# Main Program
def main():
    # Create instances of different vehicles
    car = Car("Sedan")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")
    train = Train("Freight Train")

    # Store all vehicles in a list
    vehicles = [car, plane, boat, train]

    # Call move() for each vehicle
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()
