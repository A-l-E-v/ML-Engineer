# Напишите программу, которая принимает два целых числа a, b и
# строку s - символ '>' или '<', и выводит числа в порядке убывания,
# если s равна '>', и в порядке возрастания, если s равна '<'

a = int(input())
b = int(input())
s = input().strip()

if s == '>':
    print(max(a, b), min(a, b))
else:
    print(min(a, b), max(a, b))