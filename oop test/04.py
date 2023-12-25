#OOP Exercise 4: Class Inheritance
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def description(self):
        print(f'{self.name} is a {self.gender} and he is {self.age} years old.') 
 
class Employee(Person):
    def __init__(self, name, age, gender, designation):
        super().__init__(name, age, gender)
        self.desigantion = designation
    
    def description(self):
        print(f'{self.name} is a {self.gender} and he is {self.age} years old and he is a {self.desigantion}.')
ab = Employee('Abdullah', 19, 'male', 'developer')
ab.description()
