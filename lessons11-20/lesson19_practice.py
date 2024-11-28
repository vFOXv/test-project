# Списки - Практика


# Задание
# Напишите программу, которая запрашивает у пользователя оценки (целые числа) для 5 студентов,
# сохраняет их в список и выводит среднюю оценку по классу.
# Также программа должна определить и вывести самую высокую и самую низкую оценку.


# Пример работы программы:

# Введите оценку студента 1: 85
# Введите оценку студента 2: 90
# Введите оценку студента 3: 78
# Введите оценку студента 4: 92
# Введите оценку студента 5: 88
#
# Средняя оценка: 86.6
# Самая высокая оценка: 92
# Самая низкая оценка: 78


# Темы:
#   - Функции input() и print() (lesson10)
#   - Условные операторы - if-else (lesson16)
#   - Цикл for (lesson18)
#   - Списки (lesson19)

# Ваше решение:


my_list = list()
while len(my_list) < 5:
    grade = input("Enter person's grade(1-5): ")
    if grade.isdigit() and (int(grade) <= 5) and (int(grade) >= 1):
        my_list.append(int(grade))
        print("Number of entered ratings are:" + str(len(my_list)))
    else:
        print("You entered incorrect value!")

my_average = str(sum(my_list)/len(my_list))
print("Average rating is: " + my_average)