# Set comprehensions


# Set comprehensions используются для создания множеств на основе других множеств


# Синтаксис Set comprehensions
# {<expression> for <item> in <iterable> if <condition>}


# Примеры использования Set comprehensions


# Пример копирования множества
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# numbers_copy = {number for number in numbers}  # копия множества чисел
# numbers_copy.add(11)
# print(numbers)
# print(numbers_copy)


# Пример копирования с условием
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# numbers_copy = set()
# for number in numbers:
#     if number % 2 == 0:
#         numbers_copy.add(number)
# numbers_copy = {number for number in numbers if number % 2 == 0}  # множество чисел кратных 2
# print(numbers_copy)


# Пример создание множества из двух множеств
boys = {"Peter", "Alex", "John"}
girls = {"Kate", "Liza", "Kira"}

pairs = {(boy, girl) for boy in boys for girl in girls}
print(pairs)
pairs = {(boy, girls.pop()) for boy in boys}
print(pairs)
