# Функции - Практика

# Ваше решение:
def factorial(number):
    result = number
    while number > 1:
        number -= 1
        result *= number
    return result

print(factorial(5))

# Ваше решение:
def fibonacci(number):
    if number == 1 or number == 2:
        return 1

    last_two_numbers = [1, 1]

    for _ in range(number - 2):
        last_two_numbers = [last_two_numbers[1], last_two_numbers[0] + last_two_numbers[1]]

    return last_two_numbers[1]

print(fibonacci(10000))