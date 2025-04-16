# Вы получили файл movies.csv с информацией о фильмах. Каждая
# строка представляет собой запись о фильме, а столбцы содержат
# следующую информацию: "Название", "Год выпуска", "Жанр",
# "Режиссер", "Сборы (в миллионах долларов)".
# Напишите программу, которая считывает информацию из данного файла.
# В первой строке требуется вывести общее количество фильмов в файле.
# Во второй строке выведите суммарные сборы фильмов, выпущенных
# после 2010 года. В третьей строке выведите название, год выпуска и
# режиссера фильма с самыми высокими сборами.

import csv

def analyze_movies(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        
    total = len(data)
    revenue_after_2010 = sum(float(row['Сборы (в миллионах долларов)']) 
                          for row in data if int(row['Год выпуска']) > 2010)
    highest_grossing = max(data, key=lambda x: float(x['Сборы (в миллионах долларов)']))
    
    print(total)
    print(int(revenue_after_2010))
    print(highest_grossing['Название'], highest_grossing['Год выпуска'], 
          highest_grossing['Режиссер'])

analyze_movies('movies.csv')