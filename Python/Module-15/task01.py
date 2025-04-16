# Вы решили стать волшебником фотофильтров и создать свой уникальный
# эффект для изображений. Для этого требуется написать функцию
# apply_magic_filter(image, brigthness, color, contrast), которая принимает на
# вход изображение и параметры для усиления яркости, цвета и контраста.
# Пошаговый план решения задачи:
# 1 шаг
# Загрузите модули Image, ImageEnhance из библиотеки PIL
# 2 шаг
# Создайте функцию с требуемым заголовком
# 3 шаг
# Внутри функции последовательно для яркости, цвета и контраста
# примените конструкцию:
# image = ImageEnhance.<тип фильтра>(image).enhance(<степень
# усиления>)
# <тип фильтра> - это Brightness, Color или Contrast соответственно
# <степень усиления> - это положительное число типа float,
# которое вы передаете в качестве параметров функции
# 4 шаг
# Верните новое измененное изображение
# как результат работы функции
# Протестируйте работу функции на произвольном
# изображении с различными параметрами

from PIL import Image, ImageEnhance

def apply_magic_filter(image_path, brightness=1.0, color=1.0, contrast=1.0, output_path='output-cats.jpg'):
    try:
        # Открываем изображение
        image = Image.open(image_path)
        
        # Применяем фильтры
        image = ImageEnhance.Brightness(image).enhance(brightness)
        image = ImageEnhance.Color(image).enhance(color)
        image = ImageEnhance.Contrast(image).enhance(contrast)
        
        # Сохраняем результат
        image.save(output_path)
        print(f"Изображение сохранено как {output_path}")
        return image
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Пример использования
apply_magic_filter('input-cats.jpg', brightness=1.5, color=1.2, contrast=1.3)
