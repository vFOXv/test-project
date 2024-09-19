# Set comprehensions - Практика #1

orders = [
    ("iPhone 13", 900),
    ("Samsung Galaxy", 700),
    ("iPhone 13", 900),
    ("MacBook Air", 1100),
    ("HP Pavilion", 800),
    ("Samsung Galaxy", 700),
    ("Dell Desktop", 750),
    ("MacBook Air", 1100),
    ("Apple iMac", 1500),
    ("Dell Desktop", 750),
]

# Множество уникальных товаров
unique_items = {order[0] for order in orders}
print(unique_items)

# Множество товаров, которые были заказаны более одного раза
items_ordered_more_than_once = {order[0] for order in orders if orders.count(order) > 1}
print(items_ordered_more_than_once)

# Множество уникальных цен
unique_prices = {order[1] for order in orders}
print(unique_prices)

# Множество товаров, цена которых превышает $1000
items_over_1000 = {order[0] for order in orders if order[1] > 1000}
print(items_over_1000)


# Set comprehensions - Практика #2

attendance_data = [
    {"student": "Alice", "courses": {"Math", "Physics", "Chemistry"}},
    {"student": "Bob", "courses": {"Math", "Biology", "Chemistry"}},
    {"student": "Charlie", "courses": {"Physics", "Math", "Art"}},
    {"student": "David", "courses": {"History", "Math", "Art"}},
    {"student": "Eve", "courses": {"History", "Physics", "Math"}},
    {"student": "Shon", "courses": {"History", "Art"}}
]

# Найти множество всех уникальных курсов, которые посещают студенты
unique_courses = {course
                  for data in attendance_data
                  for course in data["courses"]}
print(unique_courses)

# Найти множество студентов, посещающих курсы, которые также посещает студент "Alice"
search_result = [data for data in attendance_data if data["student"] == "Alice"]
alice_courses = search_result[0]["courses"] if search_result else set()
students = {data["student"]
            for data in attendance_data
            if data["student"] != "Alice" and alice_courses.intersection(data["courses"])}
print(students)