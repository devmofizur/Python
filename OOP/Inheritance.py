class Vehicle:
    def general_usage(self):
        print("General use : Transportation")
    def runs_on(self):
        print("I run on oil")

class Car(Vehicle):
    def __init__(self):
        print("I am car")

        self.wheels = 4
        self.has_roof = True
    
    def general_usage(self):
        print("General use : Commute to work")

    def specific_usage(self):
        self.general_usage()
        Vehicle.general_usage(self)
        print("Specific use : Family vacation")
        

class Bike(Vehicle):
    def __init__(self):
        print("I am bike")

        self.wheels = 2
        self.has_roof = False
    
    # def general_usage(self):
    #     print("General use : Roaming")
    def specific_usage(self):
        print("Specific use : Solo,duo fast travel, road trip")

c = Car()
c.runs_on()
c.specific_usage()

b = Bike()
b.runs_on()
b.general_usage()