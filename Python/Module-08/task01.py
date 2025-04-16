# Вам необходимо написать генератор квадратов целых чисел, который
# возвращает при каждом вызове следующий квадрат (первый квадрат - 0)
# Формат ввода
# -
# Формат вывода
# Генератор, возвращающий следующий квадрат

def square_gen():
    n = 0
    while True:
        yield n ** 2
        n += 1

g = square_gen()
print(next(g))
print(next(g))
print(next(g))
print('\n')
g = square_gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
