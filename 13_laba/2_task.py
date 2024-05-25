def multiply_matrices(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                
    return C

import multiprocessing

def split_matrix(matrix, size):
    """Разделяет матрицу на подматрицы размером size x size."""
    submatrices = []
    for i in range(0, len(matrix), size):
        row_submatrix = matrix[i:i+size]
        for j in range(0, len(row_submatrix[0]), size):
            submatrix = [row[j:j+size] for row in row_submatrix]
            submatrices.append(submatrix)
    return submatrices

def parallel_multiply(matrices, pool_size):
    """Параллельно перемножает матрицы с использованием указанного количества процессов."""
    if len(matrices) == 1:
        return matrices[0]

    pool = multiprocessing.Pool(processes=pool_size)
    result = []

    for i in range(len(matrices)-1):
        for j in range(i+1, len(matrices)):
            submatrices_i = split_matrix(matrices[i], pool_size)
            submatrices_j = split_matrix(matrices[j], pool_size)

            partial_results = pool.starmap(multiply_matrices, [(sub_i, sub_j) for sub_i in submatrices_i for sub_j in submatrices_j])
            
            result.extend(partial_results)

    pool.close()
    pool.join()

    return result

# Пример использования
if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

    result = parallel_multiply([A, B], 4)  # Используем 4 процесса

    print("Результат:")
    for row in result:
        print(row)

