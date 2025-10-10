class Person:
    
    def __init__(self, name = "empty", age = "mepty"): # Default primary opposites
        self.name = name
        self.age  = age   
    
    def work(self):
        print(f"{self.name} is working...")
        
        
# __init__ , __str__, ...  -->  magic method        
        
O1 = Person("sadegh", 20)
O1.work()
O1.city = "Birjand"  # add a new atribut
O1.age = "45"        # update age atribut
print(O1.age)


O2 = Person("ali", 19)
O2.work()
print(O2.name)


O3 = Person()
O3.work()