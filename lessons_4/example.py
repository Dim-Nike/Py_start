#------TRIGGER__PY_START------

words = {'short': 'Гоша', 'long': 'Георгий'}
print(words['long'])

list = [5, "Stroka", True, 5.23, 7] # list
# list[1] = 12
list.append("Привет")
b = [5, 8, 1, 9, 6]
list.extend(b)
list.remove(5)
list.remove(5)
list.pop(0)
b.reverse()
b.clear()
list.extend([6, 2, 9, True])
# print(b)
# print(list[::3])
print(list[::])

cor = (5, "Stroka", True, 5.23, 7)
# cor[0] = 6 # Нельзя
# print(cor[0])

mult = set(list)
print(mult)

f_mult = frozenset(list)
print(f_mult)


#-------HOMEWORK--------

# TODO Список и кортеж
#  Создайте программу, которая будет принимать числа от пользователя и объединять их в список, а также в кортеж.

# TODO Клонирование списка
#  Создайте программу, которая будет копировать или клонировать список.

# TODO Вложенный список
#  Создайте список и выведите каждый его элемент на экран при помощи нескольких циклов for.
#  Список данных:
list_1 = [[2, 5, 6], [5, 7, 1], [3, 6, 7, 34, 7, 0]]


# TODO Работа со спискам
#  Создайте функцию, которая будет принимать список данных и возвращать новый список состоящий из первого и последнего элемента переданного в функцию.
#  Список данных:
a = [5, 10, 15, 20, 25]
# Должны получить список [5, 25]


# TODO Простейшие списки

# TODO Задание 1: Создайте список при помощи цикла for, который будет состоять из 5 элементов.

# TODO Задание 2: Создайте пустой список и выполните над ним операции:
#  добавьте в него число 5 и -6
#  добавьте в него целиком весь первый список
#  выполните сортировку списка
#  Выведите на экран оба списка без использования циклов.


# TODO Наименьший элемент
#  Есть список чисел:
#  lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
#  Найдите самый маленький элемент списка и переместите его в зависимости от условия:
#  если найденный элемент меньше за ноль, то поместите его в конец списка
#  если найденный элемент больше или равен нулю, то поместите его в начало списка.
#  Важно: нахождение минимального элемента осуществите без использования встроенных функций в Python.


# TODO Использование индексов
#  Выведите в списке третий элемент с конца.
#  Список:
list_index = [3.4, 56, "Some", "Hi", 7, 3.8, 44]