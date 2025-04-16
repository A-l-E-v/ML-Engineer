# Вы решили создать свою собственную мозаичную картину, используя
# изображение и технику пиксельного искусства. Нужно разбить входное
# изображение на маленькие квадратные блоки, каждый из которых будет
# представлять определенный цвет и покрасить весь блок в требуемый
# цвет. Для этого требуется написать функцию create_pixel_art(image,
# block_size), которая принимает на вход изображение и размер стороны
# квадрата пикселизации. Излишнюю часть изображения справа и снизу
# требуется откадрировать с помощью функции crop таким образом, чтобы
# ширина и высота были кратными block_size.
# Пошаговый план решения задачи:
# 1 шаг
# Загрузите изображение с помощью PIL и передайте в функцию
# 2 шаг
# Установите размер блоков (например, 10x10 пикселей)
# для разбиения изображения
# 3 шаг
# Обрежьте правую и нижнюю части входного изображения
# так, чтобы ширина и высота были кратными размеру блока
# 4 шаг
# Пройдите по каждому блоку изображения и найдите средний цвет блока
# 5 шаг
# Замените все пиксели внутри блока на этот средний цвет
# 6 шаг
# Верните новое изображение в виде мозаичной картины
# Примечание:

# Используйте вложенные циклы для обхода блоков, функцию
# Image.crop(box) для обрезания очередного блока изображения, здесь
# box = (x, y, x + block_size, y + block_size) является прямоугольником,
# задающим границы блока.
# Для расчета среднего цвета пикселя, требуется пройтись по всем
# пикселям блока и отдельно рассчитать средние арифметические
# значения для красного, зеленого и синего каналов внутри блока.
# Затем используйте функцию Image.paste((r, g, b), box) для вставки
# нужного цвета в блоке.

from PIL import Image

def create_pixel_art(image_path, block_size=10, output_path='cats-pixel_art.jpg'):
    try:
        image = Image.open(image_path)
        width, height = image.size
        
        # Обрезаем изображение до кратного block_size
        new_width = width - (width % block_size)
        new_height = height - (height % block_size)
        image = image.crop((0, 0, new_width, new_height))
        
        # Создаем новое изображение для мозаики
        pixel_art = Image.new('RGB', (new_width, new_height))
        
        # Обрабатываем каждый блок
        for y in range(0, new_height, block_size):
            for x in range(0, new_width, block_size):
                box = (x, y, x + block_size, y + block_size)
                block = image.crop(box)
                
                # Вычисляем средний цвет блока
                r, g, b = 0, 0, 0
                pixels = block.getdata()
                for pixel in pixels:
                    r += pixel[0]
                    g += pixel[1]
                    b += pixel[2]
                
                count = len(pixels)
                avg_color = (r // count, g // count, b // count)
                
                # Закрашиваем блок средним цветом
                for dy in range(block_size):
                    for dx in range(block_size):
                        pixel_art.putpixel((x + dx, y + dy), avg_color)
        
        pixel_art.save(output_path)
        print(f"Пиксельная арт сохранена как {output_path}")
        return pixel_art
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Пример использования
create_pixel_art('input-cats.jpg', block_size=20)