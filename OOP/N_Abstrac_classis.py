# تبعیت کردن وارث از قوانین
from abc import ABC, abstractmethod

# نباید امکانارث بری از کلاس مادر باشه 
class Animal(ABC):
    def eat(self):
        return "Eat"
    
    @abstractmethod
    def make_sound(self):
        pass

# در ساب کلاس ها چه مد هایی باید تعریف یشوند 
class Dog(Animal):   # --> sub class(Animal)
    def make_sound(self):
        return "Woof!"
    
    
class Cat(Animal):   # --> sub class(Animal)
    def make_sound(self):
        return "Meow!"
    
    
class Sheep(Animal): # --> sub class(Animal)
    def make_sound(self):
        return "Bah!"
    
    
class Mous(Animal):
    pass    
    
    
    
O0 = Sheep()
x = O0.make_sound()
print(x)

O1 = Animal()
O2 = Mous()