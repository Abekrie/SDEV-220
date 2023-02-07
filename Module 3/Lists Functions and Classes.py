### Caleb A Rivich
### February 6, 2023
### Lists, Functions, and Classes

## This program is to gather user input and output it in fashion
# Creating the superclass "Vehicle()" and defining vehicle type "ty"

class Vehicle():
    def __init__(self, ty):
        self.__ty = ty

# Class Attribute Accessor

    def get_ty(self):
        return self.__ty

# Creating the subclass "Automobile(Vehicle)" and defining more attributes

class Automobile(Vehicle):
    def __init__(self, ty, year, make, model, doors, roof):
        Vehicle.__init__(self,ty)
        
        self.__year = year
        self.__make = make
        self.__model = model
        self.__doors = doors
        self.__roof = roof

# Creating the method to display all information

    def info(self):
        print('Vehicle type:', Vehicle.get_ty(self))
        print('Year:', self.__year)
        print('Make:', self.__make)
        print('Model:', self.__model)
        print('Number of doors:', self.__doors)
        print('Type of roof:', self.__roof)

# User input for necessary information

vType = input('Please enter the vehicle type: ')
vYear = input('Please enter the vehicle year: ')
vMake = input('Please enter the vehicle make: ')
vModel = input('Please enter the vehicle model: ')
vDoors = input('Please enter the number of doors: ')
vRoof = input('Please enter the vehicle roof type: ')

# User input is formed into an object of the Automobile subclass
# info() method is called

myRide = Automobile(vType,vYear,vMake,vModel,vDoors,vRoof)
myRide.info()
