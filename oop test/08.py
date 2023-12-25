#OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    pass
class SchoolBus(Vehicle):
    pass
class Human:
    pass
obj1 = SchoolBus()
obj2 = SchoolBus()
print(isinstance(obj1, Human))
print(isinstance(obj2, Vehicle))
