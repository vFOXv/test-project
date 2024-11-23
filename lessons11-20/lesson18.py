# * Цикл for

# Итерируемые объекты
# str - строки
# list - списки
# tuple - кортежи
# set - множества
# dict - словари


# Синтаксис цикла for

# for <переменная> in <итерируемый_объект>:
#     <тело цикла>


# ? Пример 1. Подсчет количества букв в имени
name = "John"
letter_count = 0

for letter in name:
    letter_count += 1
    print(letter)

print(f"Количество букв в имени: {letter_count}")


# ? Пример 2. Использование условий в цикле
sentence = "The quick brown fox jumps over the lazy dog"
words_count = 0

for char in sentence:
    if char == " ":
        words_count += 1

print(f"Количество слов в предложении: {words_count + 1}")


# ? Пример 3. Печать таблицы умножения (цикл в цикле)
numbers = "123456789"

for number_1 in numbers:
    for number_2 in numbers:
        print(int(number_1) * int(number_2), end=" ")

    print("")


# ? Пример 4. Выполнение цикла имея только требуемое количество итераций
# Функция range()
# На самом деле она имеет более сложный синтаксис,
#   но на данном этапе нам нужно знать только то,
#   что она используется для создания последовательности чисел

number = 3

for i in range(number):
    print("Привет")

