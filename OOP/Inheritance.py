class Animal:
    
    number = 1
    
    def __init__(self, name="empty" , age="mepty"):
        self.name = name
        self.age  = age
        
    def eat(self):
        print(f"{self.name} eating...")


class Mammal(Animal):
    
    def __init__(self, name, age, weight = "empty"):
        super().__init__(name, age)
        self.weight = weight
    
    def walk(self):
        print(f"{self.name} walk")    
  

class Fish(Animal):    
    
    def swim(self):
        print(f"{self.name} swiming...")
        


cat = Mammal("cat", 1)
cat.eat()


fish = Fish("goldfish", 2)
fish.swim()
