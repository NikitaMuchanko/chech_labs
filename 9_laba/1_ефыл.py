import matplotlib.pyplot as plt

class GeometricShape:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def paint(self):
        raise NotImplementedError("Subclasses must implement this method")
    


class Triangle(GeometricShape):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def perimeter(self):
        # Вычисление периметра треугольника
        return sum([self.coordinates[i][0] + self.coordinates[(i+1)%3][0] for i in range(3)])

    def area(self):
        # Вычисление площади треугольника по формуле Герона
        s = self.perimeter() / 2
        return (s * (s - self.coordinates[0][1]) * (s - self.coordinates[1][1]) * (s - self.coordinates[2][1])) ** 0.5

    def paint(self):
        # Простой пример рисования треугольника
        plt.plot([self.coordinates[0][0], self.coordinates[1][0], self.coordinates[2][0]], [self.coordinates[0][1], self.coordinates[1][1], self.coordinates[2][1]])
        plt.show()



class Rectangle(GeometricShape):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def perimeter(self):
        # Вычисление периметра прямоугольника
        return 2 * (self.coordinates[0][0] + self.coordinates[1][0])

    def area(self):
        # Вычисление площади прямоугольника
        return abs(self.coordinates[0][0] * self.coordinates[1][1] - self.coordinates[1][0] * self.coordinates[0][1])

    def paint(self):
        # Простой пример рисования прямоугольника
        plt.plot([self.coordinates[0][0], self.coordinates[1][0], self.coordinates[1][0], self.coordinates[0][0], self.coordinates[0][0]], [self.coordinates[0][1], self.coordinates[0][1], self.coordinates[1][1], self.coordinates[1][1], self.coordinates[0][1]])
        plt.show()



class Circle(GeometricShape):
    def __init__(self, center, radius):
        super().__init__([center])
        self.radius = radius

    def perimeter(self):
        # Периметр круга равен длине окружности
        return 2 * 3.14159 * self.radius

    def area(self):
        # Площадь круга
        return 3.14159 * self.radius**2

    def paint(self):
        # Простой пример рисования круга
        circle = plt.Circle((self.coordinates[0][0], self.coordinates[0][1]), self.radius)
        fig, ax = plt.subplots()
        ax.add_artist(circle)
        plt.show()

