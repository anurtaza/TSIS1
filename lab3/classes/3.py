class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self):
        self.length = float(input())
        self.width = float(input())
    def area(self):
        return self.length * self.width


x = Shape()
print("Area of Shape:", x.area())


y = Rectangle()
print("Area of Rectangle: ", y.area())

