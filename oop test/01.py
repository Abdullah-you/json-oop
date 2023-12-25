#OOP Exercise 1: Create a Class with instance attributes
class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def intro(self):
        print(f'{self.name} is a {self.gender}')

obj1 = Person('alice','female')
obj1.intro()
