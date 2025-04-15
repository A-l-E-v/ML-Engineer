# Реализовать программу, которая принимает список чисел и использует
# метод sort() для сортировки чисел в порядке возрастания

def sort_numbers(numbers):
    numbers.sort()
    return numbers

# Пример использования
input_list = [15, 7, 42, 3, 8]
print(sort_numbers(input_list))  # [3, 7, 8, 15, 42]