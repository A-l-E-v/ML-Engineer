# Сортировка трёх чисел
# Напишите программу, которая выводит последовательно три
# числа в порядке возрастания

a = int(input())
b = int(input())
c = int(input())

sorted_nums = sorted([a, b, c])
print(sorted_nums[0], sorted_nums[1], sorted_nums[2])