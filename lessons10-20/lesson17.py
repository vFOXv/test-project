# Условные операторы - if-elif-else

user_value = input("Введите любое значение: ")

if user_value.isdigit():
    print("Это число")
elif user_value.isalpha():
    print("Ваше значение содержит только буквы")
elif user_value.isalnum():
    print("Ваше значение содержит буквы и цифры")
else:
    print("Это что-то другое")
