class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(self, name, age, 'Cow')
        self.milk_produce = 0

    def milk_produce(self, amount):
        self.milk_produce += amount
        return f"{self.name} has produced {self.milk_produce} liter milk every day"
    
class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")
        self.eggs_laid = 0
    
    def lay_egg(self):
        self.eggs_laid += 1
        print(f"{self.name} laid an egg. Total eggs laid: {self.eggs_laid}")