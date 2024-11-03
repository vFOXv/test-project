# Логические операторы

# not - логическое НЕ
# and - логическое И
# or - логическое ИЛИ

print("\nЛогическое И\n" + "-" * 50)
print(True and True)
print(True and False)
print(False and False)

print("\nЛогическое ИЛИ\n" + "-" * 50)
print(True or True)
print(False or True or False or False)
print(False or False)

print("\nЛогическое НЕ\n" + "-" * 50)
print(not True)
print(not False)











# Приоритет логических операторов
# not > and > or
# print("\nПриоритет логических операторов\n" + "-" * 50)
# print(not False or False and False)
# print(True or False and False)
# print(True or False)
# print(True)


# Изменение приоритета с помощью скобок
# print("\nИзменение приоритета с помощью скобок\n" + "-" * 50)
# print(not (False or (False and False)))
# print(not (False or False))
# print(not False)
# print(True)











# Сравнение чисел
print("\nСравнение чисел\n" + "-" * 50)

# == - равенство (length == 10)
# != - неравенство (length != 10)
# > - больше
# < - меньше
# >= - больше или равно (length >= 10)
# <= - меньше или равно (length <= 10)

# print(1 == 1)
# print(1 != 1)
# print(1 > 1)
# print(1 < 1)
# print(1 >= 1)
# print(1 <= 1)














# Математическое сравнение и логические операторы
print("\nМатематическое сравнение и логические операторы\n" + "-" * 50)

# print(1 < 2 and 2 < 3)
# print(True and True)
# print(True)


# print(1 < 2 or 5 < 3)
# print(True or False)
# print(True)

# print(not 1 < 2)
# print(not True)
# print(False)

print(1 < 2 or 5 < 3 and 2 < 3)
