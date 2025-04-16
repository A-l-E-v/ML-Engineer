# Напишите программу, которая получает информацию со страницы из
# Википедии. Для этого используйте собственную функцию
# get_wikipedia_content(url) с применением библиотеки request
# Пошаговый план решения задачи
# 1 шаг
# Импортируйте библиотеку requests
# 2 шаг
# Используйте код response = requests.get(<адрес
# веб ресурса>), чтобы получить содержимое страницы
# 3 шаг
# Проверьте успешность запроса response.status_code == 200
# 4 шаг
# Если запрос успешен, требуется вернуть переменную
# response.text, в которой будет находиться ответ сервера
# 5 шаг
# Если возникает какая-либо ошибка во время выполнения запроса,
# то будет выброшено исключение requests.RequestException.

# Нужно его обработать внутри функции и вернуть строку:
# "Ошибка при получении страницы. Статус код: <статус
# код>"
# 6 шаг
# Проверьте работу функции на странице:

# https://ru.wikipedia.org/wiki/Python

import requests

def get_wikipedia_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Ошибка при получении страницы. Статус код: {response.status_code}"
    except requests.RequestException as e:
        return f"Ошибка при получении страницы. Статус код: {response.status_code}"

def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in text if char in vowels)

url = "https://ru.wikipedia.org/wiki/Python"
content = get_wikipedia_content(url)

if not content.startswith("Ошибка"):
    print(f"Количество гласных букв: {count_vowels(content)}")
else:
    print(content)