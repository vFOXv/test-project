# Set comprehensions - Практика #2


# Задание
# Используя Set Comprehensions и список attendance_data создайте следующие множества:

# - Множество уникальных курсов
# - Множество студентов, посещающих курсы, которые также посещает студент "Alice"


attendance_data = [
    {"student": "Alice", "courses": {"Math", "Physics", "Chemistry"}},
    {"student": "Bob", "courses": {"Math", "Biology", "Chemistry"}},
    {"student": "Charlie", "courses": {"Physics", "Math", "Art"}},
    {"student": "David", "courses": {"History", "Math", "Art"}},
    {"student": "Eve", "courses": {"History", "Physics", "Math"}},
    {"student": "Shon", "courses": {"History", "Art"}}
]


# Ожидаемый результат:
# {'Physics', 'History', 'Biology', 'Art', 'Chemistry', 'Math'}
# {'Eve', 'David', 'Bob', 'Charlie'}


# Найти множество всех уникальных курсов, которые посещают студенты
# Ваш код


# Найти множество студентов, посещающих курсы, которые также посещает студент "Alice"
# Ваш код