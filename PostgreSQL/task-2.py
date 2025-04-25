# Задание No2
# Подключиться к БД demo из python и сделать select
# первых ста записей из таблицы tickets
# Отобразить данные в терминале при помощи функции fetchall()
# Подключение к БД происходит также как мы делали на уроке
# Для выполнения запроса нужно использовать функцию execute

import psycopg2

try:
    print("Подключение к базе данных demo...")
    conn = psycopg2.connect(
        dbname="demo",
        user="al",
        password="aaa000",
        host="localhost"
    )
    cursor = conn.cursor()

    print("Выполнение запроса SELECT...")
    cursor.execute("SELECT * FROM bookings.tickets LIMIT 100;")
    data = cursor.fetchall()

    print("Результаты запроса:")
    for row in data:
        print(row)

    print("Запрос выполнен успешно.")
except psycopg2.Error as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Соединение с базой данных закрыто.")