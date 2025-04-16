# Напишите функцию multiply_matrices(matrix1, matrix2), которая
# принимает две матрицы (представленные в виде вложенных
# списков одинакового размера) и возвращает результат их
# умножения.

# Формат multiply_matrices(matrix1, matrix2) принимает два аргумента:
# 01 matrix1 (список) - входная матрица размером MxN,
# где M - количество строк, N - количество столбцов
# 02 matrix2 (список) - входная матрица размером NxK,
# где N - количество строк, K - количество столбцовФункция должна:
# Проверить, что количество столбцов в matrix1 равно количеству
# строк в matrix2. В случае несоответствия размеров матриц, вернуть
# пустой список
# Создать пустую матрицу result размером MxK
# Вычислить результат умножения матриц: элемент на
# позиции (i, j) в result равен сумме произведений элементов
# строки i в matrix1 и столбца j в matrix2
# Вернуть матрицу result в качестве результата

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return []
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

print(multiply_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
print(multiply_matrices([[1, 2], [3, 4], [5, 6]], [[7,8,9],[10,11,12]]))
print(multiply_matrices([[1, 2, 3], [4, 5, 6], [7,8,9]], [[1,0,0],[0,1,0],[0,0,1]]))
