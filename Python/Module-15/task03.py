# Вы решили создать геометрическую картину. Задайте размеры холста
# и превратите его в абстрактную композицию, используя разноцветные
# прямоугольники и эллипсы.
# Пошаговый план решения задачи:
# 1 шаг
# Загрузите модуль ImageDraw из библиотеки PIL, загрузите
# библиотеку random. Задайте случайное зерно random.seed(777)
# для воспроизводимости результатов
# 2 шаг
# Создайте функцию create_geometric_art(width, height),
# которая принимает на вход размеры нового изображения, а
# возвращает нарисованную композицию
# 3 шаг
# Внутри функции создайте новое изображение заданного размера:
# blank_image = Image.new("RGB", (width, height), "white")
# 4 шаг
# Создайте объект для рисования на изображении
# draw = ImageDraw.Draw(blank_image)
# 5 шаг
# В цикле последовательно создайте 100 элементов композиции и
# нанесите их на холст с помощью функций draw.rectangle и draw.ellipse
# 6 шаг
# Все параметры расположения фигур, а также их цвет должны
# быть сгенерированы случайным образом.
# Для генерации левого верхнего угла фигуры используйте
# конструкцию x, y = random.randint(0, width - 1),
# random.randint(0, height - 1)
# Для генерации ширины и высоты фигуры используйте

# size_x, size_y = random.randint(20, 100),
# random.randint(20, 100)
# 7 шаг
# Сгенерируйте случайный цвет color = (random.randint(0,
# 255), random.randint(0, 255), random.randint(0, 255))
# 8 шаг
# Сгенерируйте целое число: 0 или 1. Если выпал 0, рисуйте эллипс с
# координатами (x, y, x + size_x, y + size_y) и сгенерированным цветом
# (параметр fill). Если выпала 1, нарисуйте прямоугольник
# 9 шаг
# Верните полученное изображение в качестве
# результата работы функции

from PIL import Image, ImageDraw
import random

def create_geometric_art(width=900, height=400, output_path='geometric_art.jpg'):
    random.seed(777)  # Для воспроизводимости
    blank_image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(blank_image)
    
    for _ in range(100):
        # Генерируем параметры фигуры
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        size_x = random.randint(20, 100)
        size_y = random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Рисуем фигуру (0 - эллипс, 1 - прямоугольник)
        if random.randint(0, 1) == 0:
            draw.ellipse([x, y, x + size_x, y + size_y], fill=color)
        else:
            draw.rectangle([x, y, x + size_x, y + size_y], fill=color)
    
    blank_image.save(output_path)
    print(f"Геометрическая арт сохранена как {output_path}")
    return blank_image

# Пример использования
create_geometric_art()