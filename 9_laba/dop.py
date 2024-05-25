class Parameters:
    def __init__(self, value, description):
        self.value = value
        self.description = description


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.parameters = Parameters(self.radius, "Radius of the circle")
        
    @staticmethod
    def area(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.parameters = [
            Parameters(a, "Length of side a"),
            Parameters(b, "Length of side b"),
            Parameters(c, "Length of side c")
        ]
        
    @staticmethod
    def area(a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    @staticmethod
    def perimeter(a, b, c):
        return a + b + c

class Geometry:
    @staticmethod
    def circle_area(circle):
        return circle.area(circle.radius)
    
    @staticmethod
    def circle_perimeter(circle):
        return circle.perimeter(circle.radius)
    
    @staticmethod
    def triangle_area(triangle):
        return triangle.area(triangle.a, triangle.b, triangle.c)
    
    @staticmethod
    def triangle_perimeter(triangle):
        return triangle.perimeter(triangle.a, triangle.b, triangle.c)


class GeometryComposite:
    def __init__(self, figure):
        self.figure = figure
        
    def circle_area(self):
        return self.figure.area(self.figure.radius)
    
    def circle_perimeter(self):
        return self.figure.perimeter(self.figure.radius)
    
    def triangle_area(self):
        return self.figure.area(self.figure.a, self.figure.b, self.figure.c)
    
    def triangle_perimeter(self):
        return self.figure.perimeter(self.figure.a, self.figure.b, self.figure.c)
