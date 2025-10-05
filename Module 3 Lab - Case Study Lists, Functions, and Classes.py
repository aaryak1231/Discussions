# Name: Aaryak Bashyal
# File name: Module 3 Lab - Case Study Lists, Functions, and Classes
# Description: This app asks the user to enter details about a car such as vehicle type, year, make, model, number of doors, and type of roof, and displays the information.


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

print("Enter car details below:\n")

vehicle_type = "car"
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter type of roof (solid or sun roof): ")

car = Automobile(vehicle_type, year, make, model, doors, roof)

print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Number of doors: {car.doors}")
print(f"Type of roof: {car.roof}")