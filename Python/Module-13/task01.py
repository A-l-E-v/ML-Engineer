# Требуется создать иерархию классов для животных: базовый класс Animal,
# а затем два подкласса Mammal и Bird. Каждый из подклассов может иметь
# свои уникальные свойства и методы, а также наследовать общие от Animal.
# Класс Animal содержит атрибуты name и sound. У него должен
# быть метод make_sound, который выводит звук этого животного.
# Создайте подкласс Mammal, который наследуется от Animal.
# Добавьте ему атрибут num_legs и метод give_birth, который выводит
# сообщение о том, что млекопитающее родило потомство.
# Создайте подкласс Bird, также наследующий от Animal. Добавьте
# ему атрибут can_fly и метод fly, который выводит сообщение о том,
# что птица летит.
# Попробуйте создать несколько экземпляров
# каждого класса и вызвать их методы.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} издает звук: {self.sound}")

class Mammal(Animal):
    def __init__(self, name, sound, num_legs):
        super().__init__(name, sound)
        self.num_legs = num_legs
    
    def give_birth(self):
        print(f"{self.name} родил(а) потомство")

class Bird(Animal):
    def __init__(self, name, sound, can_fly):
        super().__init__(name, sound)
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            print(f"{self.name} летит")
        else:
            print(f"{self.name} не может летать")

# Пример использования
lion = Mammal("Лев", "Рррр", 4)
lion.make_sound()
lion.give_birth()

penguin = Bird("Пингвин", "Кря", False)
penguin.make_sound()
penguin.fly()