n1, n2, m1, m2 = int(input('Ввеедите количество столбцов первой матрицы: ')), int(input('Ввеедите количество столбцов второй матрицы: ')), int(input('Ввеедите количество строк первой матрицы: ')), int(input('Ввеедите количество строк второй матрицы: '))  # при изменении файлов matrix1.txt и matrix2.txt настоятельно требуется изменить вручную эти данные.

new_elem_flag = True
curr_summands_count = 0
new_row_flag = False
curr_elems_in_a_row = 0
curr_seek = 0

with open('matrix_res.txt', 'w') as f:
    pass

for i in range(m1 * n2 * n1):
    with open('matrix1.txt', 'r') as matrix1:
        curr_el_1 = int([i.strip().split() for i in matrix1.readlines()][i // (n2 * n1)][i % n1])
        with open('matrix2.txt', 'r') as matrix2:
            curr_el_2 = int([i.strip().split() for i in matrix2.readlines()][i % m2][(i // m2) % n2])
            with open('matrix_res.txt', 'r+') as matrix_result:
                if new_row_flag:
                    matrix_result.seek(curr_seek)
                    matrix_result.write('\n')
                    curr_seek += 1
                    new_row_flag = False

                if new_elem_flag:
                    matrix_result.seek(curr_seek)
                    matrix_result.write(' ')
                    curr_seek += 1
                    matrix_result.write(str(curr_el_1 * curr_el_2))
                    curr_summands_count += 1
                    new_elem_flag = False
                else:
                    curr_res_el = [i.strip().split() for i in matrix_result.readlines()][-1][-1]
                    matrix_result.seek(curr_seek, 0)
                    matrix_result.write(str(int(curr_res_el) + curr_el_2 * curr_el_1))
                    curr_summands_count += 1

                if curr_summands_count == n1:
                    new_elem_flag = True
                    curr_summands_count = 0
                    curr_elems_in_a_row += 1
                    curr_seek += len(str(int(curr_res_el) + curr_el_2 * curr_el_1))

                if curr_elems_in_a_row == m1:
                    new_row_flag = True
                    curr_elems_in_a_row = 0

# Программа может работать с любыми размерами матриц, но форматированный вывод работает только для 3*3 х 3*3
if n1 == n2 == m1 == m2 == 3:
    with open('matrix1.txt', 'r') as mat1:
        with open('matrix2.txt', 'r') as mat2:
            with open('matrix_res.txt', 'r') as mat_res:
                mat1_read = mat1.readlines()
                mat2_read = mat2.readlines()
                matres_read = mat_res.readlines()
                for i in range(max(m1, m2, n1, n2)):
                    if i < m1 and i < m2:
                        if i == m1 // 2:
                            print(
                                f'{mat1_read[i].strip():5s}   X   {mat2_read[i].strip():5s}   =   {matres_read[i].strip()}')
                            continue
                        print(
                            f'{mat1_read[i].strip():5s}       {mat2_read[i].strip():5s}       {matres_read[i].strip()}')
                    elif i < m1:
                        print(f'{mat1_read[i].strip():10f} {matres_read[i].strip()}')