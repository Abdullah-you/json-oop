#OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Person:
    a = 'Human'
    def __init__(self):
        print(f'I am {self.a}')
class Labour(Person):
    def __init__(self):
        print(f'I am {self.a}')
obj1 = Labour()
