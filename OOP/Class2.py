class Person:
    
    def __init__(self, name = "empty", age = "mepty"): # Default primary opposites
        self.name = name
        self.age  = age   
    
    def work(self):
        print(f"{self.name} is working...")
        
    def __eq__(self, other):
        if self.name == other.name:
            if self.age == other.age: return 

O1 = Person("sadegh", 20)
O2 = Person("sadegh", 20)

print(O1 == O2)


 