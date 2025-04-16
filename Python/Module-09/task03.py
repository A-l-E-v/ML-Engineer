# Напишите функцию sum_matrix_second_diagonal, которая принимает в
# качестве аргумента квадратную матрицу чисел (представленную как
# вложенный список списков) и возвращает сумму элементов, находящихся
# под главной диагональю матрицы

def sum_matrix_second_diagonal(matrix):
    total = 0
    for i in range(1, len(matrix)):
        j = i - 1
        if j < len(matrix[i]):  # Проверяем, чтобы не выйти за границы строки
            total += matrix[i][j]
    return total

print(sum_matrix_second_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 12 (4 + 8)
print(sum_matrix_second_diagonal([[1, 2], [7, 8]]))  # 7
print(sum_matrix_second_diagonal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # 15 (5 + 9 + 10)
print(sum_matrix_second_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # 24 (4 + 7 + 8 + 10 + 11 + 12)
