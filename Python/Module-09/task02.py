# Напишите функцию count_even_numbers, которая принимает в качестве
# аргумента вложенный список чисел. Функция должна подсчитать
# количество четных чисел во всех вложенных списках и вернуть
# результат. Проверьте ваше решение для различных вложенных списков
# разной степени вложенности и содержания

def count_even_numbers(nested_list):
    count = 0
    for element in nested_list:
        if isinstance(element, list):
            count += count_even_numbers(element)
        elif isinstance(element, int) and element % 2 == 0:
            count += 1
    return count

print("[1, 2, [3, 4, [5, 6]], 7, [8]]",count_even_numbers([1, 2, [3, 4, [5, 6]], 7, [8]]))  # 4
print("[1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]]",count_even_numbers([1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]]))  # 5
print("[1, 2, 3.14, 4, 5, 6, 7]", count_even_numbers([1, 2, 3.14, 4, 5, 6, 7]))  # 3