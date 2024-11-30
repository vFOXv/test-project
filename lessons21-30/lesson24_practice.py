# Ключевое слово else в циклах for и while - Практика


# Задание:
# Данное задание предполагает 2 решения:
#   1) с использованием цикла for
#   2) с использованием цикла while
# Напишите программку, которая определяет является ли введённое пользователем число простым.
# Простое число - число, которое делится только на себя и на единицу.
# Если число простое, то программа должна вывести "<number> является простым числом".
# Если число не простое, то программа должна вывести "<number> не является простым числом".


# Ожидаемый результат:

# Введите число: 5
# 5 является простым числом
#
# Введите число: 6
# 6 не является простым числом


# Темы:
#   - Приведение типов (lesson6)
#   - Функции input и print (lesson10)
#   - Условные операторы - if-else (lesson16)
#   - Цикл for (lesson18)
#   - Цикл while (lesson23)
#   - Ключевое слово else в циклах for и while (lesson24)


# Ваше решение:

my_str = ''

while True:
    my_str = input('Enter number: ')
    if not my_str.isdigit():
        print("You didn't enter number!")
        continue
    else:
        break

number = int(my_str)

for iter in range(number):
    if (number%(iter+1) == 0) and (0 < iter < number-1):
        print('FOR///The number you entered is not prime!')
        break
else:
    print('FOR///The number you entered is prime!')

i = 1
while i < number:
    if (number%i == 0) and (1 < i < number):
        print('WHILE/The number you entered is not prime!')
        break
    i += 1
else:
    i = number
    print('WHILE/The number you entered is prime!')
