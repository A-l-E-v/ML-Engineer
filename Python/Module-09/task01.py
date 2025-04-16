# Напишите функцию flatten_list, которая принимает в качестве аргумента
# вложенный список и возвращает список, состоящий из всех элементов
# исходного списка без вложенности. Убедитесь, что ваше решение
# правильно работает для различных вложенных списков разной степени
# вложенности

def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

print(flatten_list([1, 2, [3, 4, [5, 6]], 7, [8]]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(flatten_list([1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(flatten_list([1, 2, 3.14, 4, 5, 6, 7, 8, 9]))  # [1, 2, 3.14, 4, 5, 6, 7, 8, 9]