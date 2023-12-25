#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, model, tyres, doors):
        self.model = model
        self.tyres = tyres
        self.doors = doors
    def specification(self):
        print(f'{self.model} is a type of vehicle having {self.tyres} tyres and containing {self.doors} doors')
 
class Bus(Vehicle):
    def __init__(self, model, tyres, doors):
        super().__init__(model, tyres, doors)

    def specification(self):
        super().specification()
        
bus1 = Bus('Bus',4,2)
bus1.specification()
