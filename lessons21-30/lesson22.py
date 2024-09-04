# Кортежи (tuple)


# Кортежи лучше всего использовать, когда:
# 1. Необходимо гарантировать неизменяемость данных.
# 2. Важна производительность.


# Синтаксис кортежей
# (value1, value2, value3, ...)


# Методы кортежей

# len() - возвращает количество элементов в кортеже
# index() - возвращает индекс первого вхождения элемента
# count() - возвращает количество вхождений элемента
# max() - возвращает максимальное значение
# min() - возвращает минимальное значение
# + - объединение кортежей
# * - умножение кортежей
# sorted() - сортирует кортеж


# Примеры использования кортежей

boys_height = (196, 177, 179, 185, 182, 177, 183)
girls_height = (171, 169, 175, 165, 172)
weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
months = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
books = [
    ("Гарри Поттер", "Джоан Роулинг"),
    ("Марсианские бои", "Эрих Мария Ремарк"),
    ("Властелин Колец", "Джон Толкин"),
    ("Таинственный остров", "Харуки Мураками"),
]


products = ["Молоко", "Сыр", "Мясо"]

for i, product in enumerate(products, start=1):
    print(f"{i}. {product}")


# Примеры использования методов кортежей


# len() - возвращает количество элементов в кортеже
print(len(boys_height))
print(len(girls_height))


# index() - возвращает индекс первого вхождения элемента
print(books.index(("Властелин Колец", "Джон Толкин")))


# max() - возвращает максимальное значение
girls_max_height = max(girls_height)
print(girls_max_height)


# min() - возвращает минимальное значение
boys_min_height = min(boys_height)
print(boys_min_height)


# count() - возвращает количество вхождений элемента
print(boys_height.count(boys_min_height))


# + - объединение кортежей
command_participants_height = boys_height + girls_height
print(boys_height)
print(girls_height)
print(command_participants_height)


# * - умножение кортежей
print(girls_height * 2)
print(girls_height)


# sorted() - сортирует кортеж
print(tuple(sorted(boys_height)))
print(tuple(sorted(girls_height)))
print(sorted(books))

