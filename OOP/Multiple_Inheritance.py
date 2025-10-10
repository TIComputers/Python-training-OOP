class Parent1:
    def feature1(self):
        print("Feature 1")

    def comman(self):
        print("c comman parent1")
        
        
class Parent2:
    def feature2(self):
        print("Feature 2")

    def comman(self):
        print("c comman parent2")


class Child(Parent1, Parent2):
    def feature3(self):
        print("Feature 3")
        
    def comman(self):
        print("c comman child")
        
        
child = Child()

child.feature1()
child.feature2()
child.feature3()

child.comman()