# Аргументы функций


# Порядок аргументов в функциях

# Позиционные аргументы
# *args (произвольное количество позиционных аргументов)
# Именованные аргументы со значениями по умолчанию
# **kwargs (произвольное количество именованных аргументов)


# Позиционные аргументы
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


# *args (произвольное количество позиционных аргументов)
def summarize(*numbers):
    return sum(numbers)


print(summarize())
print(summarize(1, 2, 3))
print(summarize(10, 20, 30, 40))


items_by_category = {}


def add_items_to_category(category, *items):
    if category in items_by_category:
        items_by_category[category].extend(items)
    else:
        items_by_category[category] = list(items)


add_items_to_category("smartphones", "iPhone 13", "Samsung Galaxy", "Xiaomi Mi 11")
add_items_to_category("laptops", "MacBook Air", "HP Pavilion", "Dell XPS 13")
add_items_to_category("smartphones", "Apple iMac", "HP Envy Desktop")

for category, items in items_by_category.items():
    print(f"{category}: {items}")

# Именованные аргументы со значениями по умолчанию
def greet(name, greeting="Hello", age=18):
    return f"{greeting}, {name}! On the form, you indicated that you were {age} years old. Is that correct?"

print(greet("Alice"))
print(greet("Bob", "Hi", 20))
print(greet("Tom", age=25))


# **kwargs (произвольное количество именованных аргументов)
def print_info(name, *data, age=30, **info):
    print(f"Name: {name}, Age: {age}")
    for value in data:
        print(f"Data: {value}")
    for key, value in info.items():
        print(f"{key}: {value}")

print_info("Alice", age=25, city="New York")


# Комбинированные аргументы
def full_info(name, *args, age=30, **kwargs):
    print(f"Name: {name}, Age: {age}")
    print("Additional arguments:", list(args))
    print("Keyword arguments:", kwargs)

full_info("Alice", "Student", "Likes Python", age=25, country="USA", hobby="Coding")




