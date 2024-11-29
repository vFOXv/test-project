# Цикл while - Практика


# Задание:
# Используя random вам нужно сгенерировать случайное число от 1 до 100.
# В цикле while, который должен быть бесконечным,
# при каждой итерации нужно просить пользователя угадать число.
# Если пользователь ввёл число меньше загаданного, вывести "Ваше число меньше загаданного".
# Если пользователь ввёл число больше загаданного, вывести "Ваше число больше загаданного".
# Если пользователь ввёл число равно загаданному, вывести "Вы угадали!" и выйти из цикла while.
# При этом, если пользователь ввёл 'exit', вывести "Вы вышли из игры" и выйти из цикла while.


# Ожидаемый результат:

# Введите число: 50
# Ваше число меньше загаданного
#
# Введите число: 75
# Ваше число больше загаданного
#
# Введите число: 71
# Вы угадали!


# Темы:
#   - Приведение типов (lesson6)
#   - Функции input и print (lesson10)
#   - Условные операторы - if-elif-else (lesson17)
#   - Цикл while (lesson23)


import random

number = random.randint(1, 100)

# Ваше решение:

while True:
    attempt = input('Enter your number from 1 to 100: ')
    if attempt == 'exit':
        print('You are out from the game!')
        break
    elif int(attempt)<number:
        print('Your number less than the hidden number!')
    elif int(attempt)>number:
        print('Your number big than the hidden number!')
    elif int(attempt) == number:
        print('You guessed in right!')
        break
