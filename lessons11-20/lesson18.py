# Цикл for

# Итерируемые объекты
# str - строки
# list - списки
# tuple - кортежи
# set - множества
# dict - словари


# Синтаксис цикла for

# for <переменная> in <итерируемый_объект>:
#     <тело цикла>
















# name = "John"
# letter_count = 0
#
# for letter in name:
#     letter_count += 1
#
# print(f"Количество букв в имени: {letter_count}")











numbers = "123456789"

for number_1 in numbers:
    for number_2 in numbers:
        print(int(number_1) * int(number_2), end=" ")

    print("")
