# Дана строка, состоящая из букв (представляющих собой числа),
# разделенных запятой. Напишите программу, которая преобразует эту
# строку в список чисел, затем создает новый список, содержащий
# квадраты четных чисел и их попарные произведения (если есть хотя бы
# два четных числа). Если четных чисел меньше двух, то программа
# возвращает строку, состоящую из элементов исходного списка,
# объединенных символом "-". В реализации программы необходимо
# использовать методы split и join, а также конструкцию list(строка)

def process_string(s):
    # Преобразуем строку в список, оставляя все элементы как строки
    elements = [elem.strip() for elem in s.split(',')]
    
    # Фильтруем только цифры и преобразуем в числа
    numbers = []
    for elem in elements:
        if elem.isdigit():
            numbers.append(int(elem))
    
    # Получаем четные числа
    even_numbers = [x for x in numbers if x % 2 == 0]
    
    if len(even_numbers) >= 2:
        # Квадраты четных чисел
        squares = [x**2 for x in even_numbers]
        # Произведения пар (только последовательных пар)
        products = []
        for i in range(len(even_numbers)-1):
            products.append(even_numbers[i] * even_numbers[i+1])
        return squares + products
    else:
        return '-'.join(elements)

# Примеры использования
input_str1 = "a, 2, b, 4, c, 5, d, 8, e, 9"
print(process_string(input_str1))  # [4, 16, 64, 8, 32]

input_str2 = "a, 2, b, 3, c, 5, d, 7, e, 11"
print(process_string(input_str2))  # a-2-b-3-c-5-d-7-e-11