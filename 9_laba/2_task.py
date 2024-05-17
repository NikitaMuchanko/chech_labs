from copy import deepcopy

class Matrix:
    def __init__(self, matrix_list):
        # Глубокое копирование списка списков
        self.matrix = deepcopy(matrix_list)

    def __str__(self):
        # Преобразование матрицы в строку
        result = ""
        for row in self.matrix:
            result += "\t".join(map(str, row)) + "\n"
        return result.rstrip("\n")  # Удаляем лишний перенос строки в конце

    @property
    def size(self):
        # Возвращаем размер матрицы
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        # Сложение матриц
        if not isinstance(other, Matrix) or self.size!= other.size:
            print("Ошибка: матрицы не могут быть сложены.")
            return None
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.size[1])] for i in range(self.size[0])])

    def __mul__(self, other):
        # Умножение матриц
        if isinstance(other, (int, float)):
            return Matrix([[cell * other for cell in row] for row in self.matrix])
        elif isinstance(other, Matrix) and self.size[1] == other.size[0]:
            return Matrix([[sum(a*b for a, b in zip(row1, col2)) for col2 in zip(*other.matrix)] for row1 in self.matrix])
        else:
            print("Ошибка: матрицы не могут быть перемножены.")
            return None

    def __rmul__(self, other):
        # Умножение матрицы на скаляр справа
        return self.__mul__(other)

    @staticmethod
    def transposed(matrix):
        # Транспонирование матрицы
        return Matrix([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])


# Создание двух матриц
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Сложение матриц
result_add = matrix1 + matrix2
print(result_add)

# Умножение матрицы на скаляр
result_mul = matrix1 * 2
print(result_mul)

# Транспонирование матрицы
transposed_matrix = Matrix.transposed(matrix1)
print(transposed_matrix)



#не могу никак решить проблему с транспонированием и умножением на скаляр....