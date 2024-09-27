# Исключения - Блоки else, finally и функция raise

# Блок else в исключениях вызывается, если в блоке try не было исключения
# Блок finally в исключениях вызывается в любом случае, включая исключения

# Функция raise в исключениях вызывает исключение с заданным сообщением


# Пример 1. Блок else

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Деление на ноль!")
except TypeError:
    print("Неправильный тип данных!")
else:
    print("Все хорошо!")


# Пример 2. Блок finally

try:
    print(10 / 2)
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    print("Все хорошо!")
finally:
    print("Конец программы!")


# Пример 3. Функция raise

try:
    first_value = input("Введите первое число: ")
    second_value = input("Введите второе число: ")

    if not first_value.isdigit() or not second_value.isdigit():
        raise ValueError("Оба значения должны быть числами!")

    first_number = int(first_value)
    second_number = int(second_value)

    if not 0 < first_number <= 10 or not 0 < second_number <= 10:
        raise ValueError("Числа должны быть в диапазоне от 1 до 10!")

    print(int(first_value) / int(second_value))
except ValueError as ex:
    print(ex)
except ZeroDivisionError:
    print("Деление на ноль!")


while True:
    try:
        age = int(input("Введите свой возраст: "))

        if age < 18:
            raise ValueError("Этот сайт доступен только для совершеннолетних!")
    except ValueError as ex:
        print(f"Ошибка регистрации: {ex}")
        continue

    try:
        sex = input("Введите свой пол: ")

        if sex != "male" and sex != "female":
            raise ValueError("Неправильное значение пола")
    except ValueError as ex:
        print(f"Ошибка регистрации: {ex}")
        continue

    print("Регистрация прошла успешно!")
    break
