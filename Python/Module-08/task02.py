# Вам необходимо написать генератор дат (каждая дата - кортеж из трех
# целых чисел: год, месяц, день), который принимает в качестве аргумента
# начальную дату и возвращает при каждом вызове следующуюФормат ввода
# Дата - кортеж из трех целых чисел (год, месяц, день)
# Формат вывода
# Генератор, возвращающий следующую дату

def date_gen(start_date):
    year, month, day = start_date
    while True:
        yield (year, month, day)
        
        # Определяем количество дней в месяце
        if month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            # Проверка на високосный год
            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                max_days = 29
            else:
                max_days = 28
        else:
            max_days = 31
        
        # Переход на следующий день/месяц/год
        if day < max_days:
            day += 1
        else:
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1

g = date_gen((2023, 10, 15))
print(next(g))
print(next(g))
print(next(g))

print("\n")

g = date_gen((2023, 11, 29))
print(next(g))
print(next(g))
print(next(g))
