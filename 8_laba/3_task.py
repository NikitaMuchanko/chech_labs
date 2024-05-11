class Vectors:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.position = [end[i] - start[i] for i in range(3)]

    def __str__(self):
        return f'{self.position}'

    def __add__(self, other):
        position = [self.position[i] + other.position[i] for i in range(3)]
        return Vectors([0, 0, 0], position)
    
    def __mul__(self, other):
        return sum(map(lambda x: x[0] * x[1], zip(self.position, other.position)))
    
    def get_length(self):
        return round(sum(map(lambda x: x**2, self.position))**0.5, 5)
    
    def get_cos(self, other):
        return round((self * other)/(self.get_length() * other.get_length()), 4)

v1 = Vectors([0, 0, 0], [1, 0, 0])
v2 = Vectors([0, 0, 0], [0, 1, 0])

print(f'Первый вектор: {v1}')
print(f'Второй вектор: {v2}')
print(f'Сумма векторов: {v1+v2}')
print(f'Скалярное произведение: {v1*v2}')
print(f'Длина вектора 1: {v1.get_length()}')
print(f'Длина вектора 2: {v2.get_length()}')
print(f'Косинус между двумя векторами: {v1.get_cos(v2)}')