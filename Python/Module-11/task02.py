# Напишите программу, которая получает информацию

# о курсе доллара США с сайта Центрального банка России
# Пошаговый план решения задачи
# 1 шаг
# Импортируйте библиотеку requests
# 2 шаг
# Используйте функцию requests.get() для получения
# содержимого страницы https://www.cbr.ru/currency_base/daily/
# 3 шаг
# Проверьте успешность запроса (статус код 200)
# 4 шаг
# Если возникло исключение обработки запроса, выведите
# сообщение: "Ошибка при выполнении запроса"
# 5 шаг
# Если запрос успешен, получите текущий курс
# доллара США с помощью следующего кода:
# index = response.text.find('Доллар США')

# index = response.text.find('<td>', index)

# index_end = response.text.find('</td>', index)

# dollar_rate = response.text[index + 4:index_end]
# Данный код находит нужный фрагмент на веб-странице и помещает
# в переменную dollar_rate строку с текущим курсом доллара США
# 6 шаг
# После выведите на экран сообщение:
# “Текущий курс доллара: <курс доллара>”

import requests

def get_dollar_rate():
    try:
        url = "https://www.cbr.ru/currency_base/daily/"
        response = requests.get(url)
        
        if response.status_code == 200:
            index = response.text.find('Доллар США')
            if index == -1:
                return "Не удалось найти курс доллара на странице"
            
            index = response.text.find('<td>', index)
            index_end = response.text.find('</td>', index)
            dollar_rate = response.text[index + 4:index_end]
            
            return f"Текущий курс доллара: {dollar_rate}"
        else:
            return f"Ошибка при выполнении запроса. Статус код: {response.status_code}"
    except requests.RequestException:
        return "Ошибка при выполнении запроса"

print(get_dollar_rate())