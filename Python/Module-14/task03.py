# Вы находитесь в таинственном мире кодированных данных. В вашем
# распоряжении есть файл"mysterious_data.json, который содержит
# ключи и значения, но все они выглядят как наборы букв и цифр.
# Напишите программу, которая считывает информацию из данного файла.
# Требуется вывести все пары в формате ключ: значение из файла в
# произвольном порядке.Для случая, когда значением является словарь, требуется идти внутрь
# словаря и выводить только те пары, значением которых является число,
# строка или список.

import json

def print_mysterious_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    def print_items(d):
        for key, value in d.items():
            if isinstance(value, (str, int, float, list)):
                print(f"{key}:{value}")
            elif isinstance(value, dict):
                print_items(value)
    
    print_items(data)

print_mysterious_data('mysterious_data.json')