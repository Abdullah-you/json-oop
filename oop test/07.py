#OOP Exercise 7: Check type of an object
class Person:
    pass
class Human(Person):
    pass
obj1 = Human()
print(type(obj1))
obj2 = Person()
print(type(obj2))