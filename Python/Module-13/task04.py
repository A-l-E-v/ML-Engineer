# Требуется создать наследника класса Calculator, класс AdvancedCalculator,
# который расширит функциональность калькулятора из предыдущей
# задачи. Новый калькулятор сможет выполнять более сложные операции
# такие как: возведение в степень и вычисление квадратного корня.
# Класс AdvancedCalculator должен содержать следующие методы:
# Метод power
# для возведения значения в степень
# Метод square_root
# для нахождения квадратного корня из значения. В случае взятия
# корня из отрицательного числа, вывести сообщение об ошибке


class Calculator:
    def __init__(self):
        self.value = 0
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def add(self, num):
        self.value += num
    
    def subtract(self, num):
        self.value -= num
    
    def multiply(self, num):
        self.value *= num
    
    def divide(self, num):
        if num == 0:
            print("Ошибка: деление на ноль")
        else:
            self.value /= num

class AdvancedCalculator(Calculator):
    def power(self, exponent):
        self.value **= exponent
    
    def square_root(self):
        if self.value < 0:
            print("Ошибка: корень из отрицательного числа")
        else:
            self.value **= 0.5

# Пример использования
adv_calc = AdvancedCalculator()

adv_calc.set_value(4)
print(adv_calc.get_value())  # 4.0
adv_calc.square_root()
print(adv_calc.get_value())  # 2.0

adv_calc.power(3)
print(adv_calc.get_value())  # 8.0

adv_calc.square_root()  # 2.828...
print(adv_calc.get_value()) 
