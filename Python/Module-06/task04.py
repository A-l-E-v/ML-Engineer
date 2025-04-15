# Программа должна принимать строку, представляющую собой табличные
# данные, разделенные запятой. Каждая строка таблицы должна быть
# отдельной строкой в входной строке. Преобразуй эту строку в список
# списков чисел, затем создай новый список, содержащий квадраты четных
# чисел из каждой строки таблицы и их суммы в каждой строке. Вложенные
# списки должны быть списками чисел, а не строками. Если в какой-то
# строке четных чисел нет, пропусти эту строку. Используй генераторы и
# вложенные списки для обработки табличных данных

def process_table(data):
    rows = data.strip().split('\n')
    result = []
    
    for row in rows:
        numbers = [int(x.strip()) for x in row.split(',') if x.strip().isdigit()]
        evens = [x for x in numbers if x % 2 == 0]
        
        if not evens:
            continue
            
        squares = [x**2 for x in evens]
        specials = []
        
        if len(evens) == 2:
            specials.append((evens[0] * evens[1] * 3) // 4)
        elif len(evens) == 3:
            specials.append((evens[0] * evens[1]) // 4)
            specials.append((evens[1] * evens[2]) // 8)
        
        result.append(squares + specials)
    
    return result

input_data = """1,2,3,4,5
10,9,8,7,6
3,6,9,12,15"""
print(process_table(input_data))