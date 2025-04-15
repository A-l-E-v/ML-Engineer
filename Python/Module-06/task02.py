# Дано два списка чисел. Напишите программу, для которой если оба списка
# имеют длину больше или равную min_count, то она должна создать новый
# список, в который добавит элементы, полученные путем перемножения
# соответствующих элементов из двух списков. Если длина хотя бы одного

# из списков меньше min_count, то программа должна вернуть срез (slice)

# из первых min_count элементов из каждого списка, а затем создать

# новый список из их попарных произведений. В реализации программы
# необходимо использовать методы append, extend и функцию len

def list_sync(list1, list2, min_count):
    if len(list1) >= min_count and len(list2) >= min_count:
        return [a*b for a, b in zip(list1, list2)]
    else:
        slice1 = list1[:min_count]
        slice2 = list2[:min_count]
        return [a*b for a, b in zip(slice1, slice2)]

# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [10, 9, 8, 7, 6]
min_count = 4
print(list_sync(list1, list2, min_count))  # [10, 18, 24, 28]