#------TRIGGER__PY_START------

class Car:
    __color = ""
    weight = 0

    def set(self, color, weight):
        self.__color = color
        self.weight = weight

class BMW (Car):
    isM_model = False

    def set(self, color, weight, isM_model):
        self._Car__color = color
        self.weight = weight
        self.isM_model = isM_model

class Mercedes (Car):
    isMaybach = False

x3 = BMW()
x3.set("Белый", 2400, False)
print(x3._Car__color)

m3 = BMW()
m3.set("Синий", 1400, True)
print(m3.isM_model)


#-------HOMEWORK--------


# TODO Простое наследование
#  Есть класс Автомобиль:

class Car:  # Создание класса
    wheels = 4  # Несколько полей
    model = "Some"
    speed = 123.5

    def set(self, wheels, model, speed):  # Метод для установки значений
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):  # Метод для вывода значений
        print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels,
              " колесах!")
        pass

# TODO Создайте класс-наследник Мотоцикл с параметрами:
#  поле с описанием двигателя - Engine;
#  метод для установки значения в поле Engine.
#  Создание объектов:
#  Создайте два объекта для класс Автомобиль и используйте оба метода для каждого из объектов.
#  Создайте объект на основе класса-наследника и используйте методы из класса Мотоцикл, а также из класса Автомобиль.


# TODO Переопределение конструктора(Повышенная сложность)
#  Есть код:

class Car_2:
    wheels = 4
    model = "Some"
    speed = 123.5

    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        self.__protected()

    def __protected(self):
        print("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")


class Motorcycle(Car_2):
    engine = "Default"

    def getAll(self):
        super().getAll()
        print("Его двигатель:", self.engine)

    def change(self, engine):
        self.engine = engine
        print("Двигатель мотоцикла установлен как: " + engine)


shkoda = Car_2(4, "Shkoda", 125.45)
shkoda.getAll()

audi = Car_2(4, "Audi", 250.9)
audi.getAll()

print("")  # Просто пропуск строки

harley = Motorcycle(2, "Harley Davidson", 200, "Powerful")
harley.getAll()

# TODO Создайте в классе наследнике конструктор, который будет вызывать конструктор главного класса,
#  а также добавлять значение engine для класса объектов Motorcycle.
