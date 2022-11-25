#Define a class
class Vehicle():
    def __init__(self,bodystyle):
        self.bodystyle=bodystyle
#inheritance of the class Vehicle to the child class Car
class Car(Vehicle):
    def __init__(self,enginetype):
        super().__init__("Car")
        self.wheels=4
        self.doors=4
        self.enginetype=enginetype
#inheritance of the class Vehicle to the child class motorcycle
class Motorcycle(Vehicle):
    def __init__(Vehicle):
        super().__init__("Motorcycle")
        if hassidecar:
            self.wheels=3
        else:
            self.wheels=2
            self.doors=1
            self.enginetype=enginetype
c=Car("H1")
print(c.wheels)
