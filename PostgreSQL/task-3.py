# Задание No3
# Переписать отображение данных с помощью функций fetchone()

# и fetchmany(). Разница заключается в том как получать данные из курсора
# fetchone() получает по одной записи, а fetchmany()
# получает заданное количество записей

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="demo",
    user="al",
    password="aaa000",
    host="localhost"
)

cursor = conn.cursor()

# Выполнение запроса
cursor.execute("SELECT * FROM tickets LIMIT 100;")

# Использование fetchone()
print("Использование fetchone():")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

# Сброс курсора для использования fetchmany()
cursor.scroll(0, mode='absolute')
print("\nИспользование fetchmany():")
rows = cursor.fetchmany(10)  # Получаем по 10 записей
while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(10)

# Закрытие соединения
cursor.close()
conn.close()