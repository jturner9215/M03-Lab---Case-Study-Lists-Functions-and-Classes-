#M03 Lab - Case Study: Lists, Functions, and Classes

class Vehicle():

    def __init__(self, type):
        self.type = type



class Automobile(Vehicle):

    def __init__(self, type, year, make, model, doors, roof):

        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof




car = Vehicle("Car")

year = int(input("\nWhat year is the car?\n"))

make = input("\nWhat is the make of the car?\n")

model = input("\nWhat is the car's model?\n")

doors = int(input("\nHow many doors does the car have?\n"))

roof = input("\nDoes the car have a sunroof?\n")

car = Automobile("car", year, make, model, doors, roof)

print("\nType: " + car.type)
print("\nYear: " + str(car.year))
print("\nMake: " + car.make)
print("\nModel: " + car.model)
print("\nNumber of doors: " + str(car.doors))
print("\nHas a sunroof? " + car.roof)

