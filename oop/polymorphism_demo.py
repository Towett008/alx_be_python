import math

#Base Class
class Shape:
    def area(self):
        #This ensures subclasses must override this method
        raise NotImplementedError("Subclasses must implement the area() method.")
    
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Override area() method 
    def area(self):
        return self.lenght * self.width 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    #override area() method
    def area(self):
        return math.pi * (self.radius ** 2)  
