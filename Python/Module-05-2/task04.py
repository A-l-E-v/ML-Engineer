# Из списка строк, в каждой из которых, целое число
# необходимо найти, наиболее часто встречающуюся цифруФормат ввода
# Вводится последовательность строк. В первой строке целое
# число N - число чисел. В каждой из последующих N строк -
# целое неотрицательное число
# Формат вывода
# Требуется вывести наиболее часто встречающуюся цифру.
# Если таких цифр несколько - вывести наибольшую из них

from collections import defaultdict

n = int(input())
digit_counts = defaultdict(int)

for _ in range(n):
    number = input().strip()
    for d in number:
        digit_counts[int(d)] += 1

max_count = max(digit_counts.values())
most_common = [d for d, count in digit_counts.items() if count == max_count]
print(max(most_common))