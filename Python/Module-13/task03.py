# Требуется создать простую программу-калькулятор
# с использованием класса Calculator, который будет
# выполнять основные арифметические операции.
# Класс Calculator должен содержать следующие методы:
# Метод set_value
# который позволяет установить текущее значение калькулятора
# Метод get_value
# который позволяет получить текущее значение калькулятора
# Методы add, substract, multiply, divide
# для сложения, вычитания, умножения и деления текущего значения
# на число. В случае деления на ноль, вывести сообщение об ошибке

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

# Пример использования
calc = Calculator()
calc.set_value(10)
calc.add(5)
print(calc.get_value())  # 15
calc.divide(0)  # Ошибка