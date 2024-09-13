# Использование списковых включений (list comprehensions)


# List comprehensions используются для создания списков на основе других списков


# Преимущества List comprehensions
# - меньше кода
# - меньше памяти (позволяют избежать создания временных переменных)
# - быстрее (по сравнению с созданием пустого списка и заполнения его в цикле)


# Синтаксис
# [<expression> for <item> in <iterable> if <condition>]


# Примеры использования List comprehensions


# Пример копирования списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_copy = [number for number in numbers]  # копия списка чисел
numbers_copy.append(11)
print(numbers)
print(numbers_copy)


# Пример копирования с условием
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_copy = []
for number in numbers:
    if number % 2 == 0:
        numbers_copy.append(number)
numbers_copy = [number for number in numbers if number % 2 == 0]  # список чисел кратных 2
print(numbers_copy)


# Пример создания списка с условием из списка словарей
products = [
    {"key": "apple", "title": "Яблоко", "price": 26, "unit": "кг", "quantity": 18},
    {"key": "pear", "title": "Груша", "price": 37, "unit": "кг", "quantity": 6},
    {"key": "orange", "title": "Апельсин", "price": 48, "unit": "кг", "quantity": 3},
    {"key": "mandarin", "title": "Мандарин", "price": 34, "unit": "кг", "quantity": 9},
    {"key": "grapefruit", "title": "Грейпфрут", "price": 210, "unit": "кг", "quantity": 15},
    {"key": "banana", "title": "Банан", "price": 23, "unit": "кг", "quantity": 12},
    {"key": "grape", "title": "Виноград", "price": 170, "unit": "кг", "quantity": 21},
]

product_keys_to_order = [product["key"] for product in products if product["quantity"] < 10]  # список ключей продуктов для заказа (продукты, количество которых < 10)

print(product_keys_to_order)


# Пример создания списка с из двух списков
boys = ["Peter", "Alex", "John"]
girls = ["Kate", "Liza", "Kira"]

pairs = [(boy, girl) for boy in boys for girl in girls]
print(pairs)
pairs = [(boy, girls[i]) for i, boy in enumerate(boys)]
print(pairs)
boys = [boy for boy in boys if len(boy) < 5]
print(boys)

# Поиск по списку словарей используя List comprehensions и next()
products = [
    {"key": "apple", "title": "Яблоко", "price": 26, "unit": "кг", "quantity": 18},
    {"key": "pear", "title": "Груша", "price": 37, "unit": "кг", "quantity": 6},
    {"key": "orange", "title": "Апельсин", "price": 48, "unit": "кг", "quantity": 3},
    {"key": "mandarin", "title": "Мандарин", "price": 34, "unit": "кг", "quantity": 9},
    {"key": "grapefruit", "title": "Грейпфрут", "price": 210, "unit": "кг", "quantity": 15},
    {"key": "banana", "title": "Банан", "price": 23, "unit": "кг", "quantity": 12},
    {"key": "grape", "title": "Виноград", "price": 170, "unit": "кг", "quantity": 21},
]

product_key_to_find = "grape"

search_result = [product for product in products if product["key"] == product_key_to_find]
product = search_result[0] if search_result else None

product = next((product for product in products if product["key"] == product_key_to_find), None)

print(product)

