# Задание No1
# Дана таблица из excel в формате .csv с разделителем ‘ , ’
# Первой строкой в таблице идут названия колонок
# Перезаписать таблицу в формате .csv в новый файл без указания
# названий столбцов и заменить разделитель на знак доллара
# После извлечения данных из файла необходимо перед записью

# в файл вызвать функцию next(), которая пропустит первую строчку

import csv

try:
    print("Начинаем чтение данных из input.csv...")
    with open('input.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем первую строку (заголовки)
        data = list(reader)

    print("Чтение завершено. Начинаем запись данных в output.csv...")
    with open('output.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='$')
        writer.writerows(data)

    print("Файл успешно перезаписан!")
except Exception as e:
    print(f"Произошла ошибка: {e}")