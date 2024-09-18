# Set comprehensions - Практика #1

# Задание
# Используя Set Comprehensions и список orders создайте следующие множества:

# - Множество уникальных товаров
# - Множество товаров, которые были заказаны более одного раза
# - Множество уникальных цен
# - Множество цен, которые были заказаны более одного раза


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


# Ожидаемый результат:
# {'Samsung Galaxy', 'Apple iMac', 'HP Pavilion', 'MacBook Air', 'Dell Desktop', 'iPhone 13'}
# {'Samsung Galaxy', 'MacBook Air', 'Dell Desktop', 'iPhone 13'}
# {800, 900, 1100, 750, 1500, 700}
# {'MacBook Air', 'Apple iMac'}


# Множество уникальных товаров
# Ваш код


# Множество товаров, которые были заказаны более одного раза
# Ваш код


# Множество уникальных цен
# Ваш код


# Множество товаров, цена которых превышает $1000
# Ваш код
