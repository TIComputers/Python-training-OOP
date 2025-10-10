# یک متد میتواند رفتار مختلفی داشته باشد بسته به اینکه کدام ابچکت داره ان را صدا میزند
from abc import ABC, abstractmethod

class UIControl(ABC):
    
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDown(UIControl):
    def draw(self):
        print("DropDown")


# polymorphism 
def draw(control):
    control.draw()
    
draw(TextBox())