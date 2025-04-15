# Напиши программу, использующую алгоритм сортировки пузырьком,
# чтобы упорядочить строки в списке строк в порядке возрастания их
# длины. Программа должна принимать входной список строк и
# сортировать его в порядке возрастания длины строк. Выведи
# промежуточный результат после каждого прохода алгоритма по списку

def bubble_sort_strings(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(strings[j]) > len(strings[j+1]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
        print(strings)  # Промежуточный результат
    
    return strings

# Пример использования
fruits = ["orange", "grape", "strawberry", "banana", "kiwi"]
print("Отсортированный результат:", bubble_sort_strings(fruits.copy()))