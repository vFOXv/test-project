# Dictionary comprehensions (включения словарей)


# Dictionary comprehensions используются для создания словарей на основе других словарей


# Синтаксис Dictionary comprehensions
# {<expression> for <key[, value]> in <iterable> if <condition>}


# Примеры использования Dictionary comprehensions

# Пример #1
# Представим, что у нас есть список товаров и их цены до скидки.
# Мы хотим создать словарь, где ключом будет название товара,
# а значением — его цена со скидкой.
# products = {
#     "iPhone": 1000,
#     "MacBook": 1500,
#     "AirPods": 200
# }
# discounted_prices = {product: price * 0.9 for product, price in products.items()}
# print(discounted_prices)


# Пример #2
# Допустим, у нас есть список студентов с их оценками,
# и мы хотим создать словарь, где ключом будет имя студента,
# а значением — его средняя оценка.
# students_grades = {
#     "Alice": [85, 92, 88],
#     "Bob": [70, 78, 82],
#     "Charlie": [90, 85, 87]
# }
# average_grades = {student: round(sum(grades) / len(grades)) for student, grades in students_grades.items()}
# print(average_grades)


# Пример #3
# Есть список книг и количества страниц в каждой из них.
# Мы хотим отфильтровать только те книги, которые длиннее 300 страниц.
# books = {"War and Peace": 1225, "1984": 328, "To Kill a Mockingbird": 281, "The Great Gatsby": 180}
# long_books = {book: pages for book, pages in books.items() if pages > 300}
# print(long_books)


# Пример #4
# Допустим, у нас есть результаты опроса по любимым видам спорта среди студентов,
# где каждому студенту присвоен идентификатор, а значение — его любимый вид спорта.
# Мы хотим создать словарь, где ключом будет вид спорта,
# а значением — количество студентов, выбравших его.
# survey_results = {
#     "student_1": "Soccer",
#     "student_2": "Basketball",
#     "student_3": "Soccer",
#     "student_4": "Tennis",
#     "student_5": "Basketball",
# }
# sport_popularity = {sport: list(survey_results.values()).count(sport) for sport in set(survey_results.values())}
# print(sport_popularity)


# Пример #5
# Предположим, у нас есть словарь отзывов клиентов,
# где ключом является идентификатор клиента,
# а значением — его оценка продукта.
# Мы хотим создать словарь, где ключом будет идентификатор клиента,
# а значением — текстовое описание оценки
# (например, "Positive" для оценок выше 3 и "Negative" для оценок ниже и равных 3).
reviews = {
    "client_1": 5,
    "client_2": 2,
    "client_3": 4,
    "client_4": 1,
    "client_5": 3
}
feedback_summary = {client: "Positive" if score > 3 else "Negative" for client, score in reviews.items()}
print(feedback_summary)