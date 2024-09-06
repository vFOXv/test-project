# Ключевое слово else в циклах for и while


# Ключевое слово else в циклах for и while используется
# для выполнения кода в случае успешного завершения цикла.


# Синтаксис использования ключевого слова else в циклах for

# for <переменная> in <итерируемый_объект>:
#     <тело цикла>
# else:
#     <код в случае успешного завершения цикла>


# Пример использования ключевого слова else в циклах for

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for number in numbers:
#     if number == 15:
#         print("Число найдено!")
#         break
# else:
#     print("Число не найдено.")


# Синтаксис использования ключевого слова else в циклах while

# while <условие>:
#     <тело цикла>
# else:
#     <код в случае успешного завершения цикла>


# Пример использования ключевого слова else в циклах while

secret_number = 7
attempts = 0

while attempts < 5:
    guess = input("\nУгадайте число от 1 до 10: ")

    if not guess.isdigit():
        print("Вы ввели не число")
        continue

    attempts += 1
    guess = int(guess)

    if guess < secret_number:
        print("Ваше число меньше загаданного")

    if guess > secret_number:
        print("Ваше число больше загаданного")

    if guess == secret_number:
        print("Поздравляю, вы угадали!")
        break
else:
    print("Вы не угадали число за 5 попыток.")