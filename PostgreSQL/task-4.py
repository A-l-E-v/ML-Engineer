# Задание No4
# Вывести в терминал 10 первых по стоимости билетов бизнес
# класса. Причем тип билета должен задаваться параметром
# (эконом, комфорт, бизнес)
# Для написания такого запроса необходимо передать параметр

# в функцию execute объекта курсор. Сделать это нужно безопасно,
# чтобы избежать sql инъекций, то через параметр метода execute и %s
# Для отображения можно воспользоваться любой
# функций семейства fetch

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

    ticket_type = "Business"  # Можно изменить на "Economy" или "Comfort"
    print(f"Поиск 10 самых дорогих билетов класса '{ticket_type}'...")

    query = """
        SELECT * 
        FROM bookings.ticket_flights 
        WHERE fare_conditions = %s 
        ORDER BY amount DESC 
        LIMIT 10;
    """
    cursor.execute(query, (ticket_type,))
    data = cursor.fetchall()

    print(f"Результаты для класса '{ticket_type}':")
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