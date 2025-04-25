# Задание No5
# Сделать так, чтобы можно было параметрически задавать значение
# таблицы и количество записей которые необходимо извлечь. Значения
# параметров должны приниматься из терминала.
# Для решения задачи удобно воспользоваться модулем sys. Он нужен для
# получения параметров. После этого параметры нужно вставить в скрипт
# посредством f нотации, так как добавлять имя таблицы, названия
# колонок и другие части SQL через execute нельзя
# Остальная часть выполняется как обычно

import sys
import psycopg2

try:
    if len(sys.argv) != 3:
        print("Использование: python script.py <table_name> <limit>")
        sys.exit(1)

    table_name = sys.argv[1]
    limit = int(sys.argv[2])

    print(f"Подключение к базе данных demo для таблицы '{table_name}'...")
    conn = psycopg2.connect(
        dbname="demo",
        user="al",
        password="aaa000",
        host="localhost"
    )
    cursor = conn.cursor()

    print(f"Выполнение запроса SELECT для таблицы '{table_name}' с лимитом {limit}...")
    query = f"SELECT * FROM bookings.{table_name} LIMIT %s;"
    cursor.execute(query, (limit,))
    data = cursor.fetchall()

    print(f"Первые {limit} записей из таблицы '{table_name}':")
    for row in data:
        print(row)

    print("Запрос выполнен успешно.")
except psycopg2.Error as e:
    print(f"Ошибка при работе с базой данных: {e}")
except ValueError:
    print("Ошибка: Лимит должен быть целым числом.")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Соединение с базой данных закрыто.")