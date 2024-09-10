# Методы словарей


# get() - возвращает значение элемента словаря по ключу
# keys() - возвращает список ключей
# values() - возвращает список значений
# items() - возвращает список пар "ключ-значение"
# update() - обновляет словарь, добавляя пары "ключ-значение"
# pop() - удаляет элемент словаря по ключу
# setdefault() - возвращает значение элемента словаря по ключу
# fromkeys() - создает словарь с заданными ключами и значениями
# copy() - создает копию словаря
# clear() - очищает словарь


user = {
    "name": "John",
    "age": 25
}


# Получаем значение элемента словаря по ключу
# dict.get(key, default=None)

# print(user.get("name"))
# print(user.get("surname"))
# print(user.get("country", "USA"))
#
# print(user["name"])
# print(user["country"])


# Получаем список ключей
# keys = user.keys()
# print(keys)
#
# keys_list = list(keys)
# print(keys_list)


# Получаем список значений
# values = user.values()
# print(values)
#
# values_list = list(values)
# print(values_list)


# Получаем список пар "ключ-значение"
# items = user.items()
# print(items)
#
# items_list = list(items)
# print(items_list)


# Добавление и изменение элементов словаря
# dict.update(other_dict)

# user.update({"age": 26, "surname": "Smith", "city": "New York"})
# print(user)
# user.update([("height", 180), ("weight", 80)])
# print(user)
#
# user["country"] = "USA"
# print(user)


# Удаление элемента словаря по ключу
# dict.pop(key, default=None)

# removed_value = user.pop("age")
# print(user)
# print(removed_value)
#
# user.pop("sex")
# removed_value = user.pop("sex", "not found")
# print(user)
# print(removed_value)


# Получаем значение элемента словаря по ключу, а если его нет, то устанавливаем указанное значение по умолчанию
# dict.setdefault(key, default=None)

# print(user.setdefault("age"))
# print(user.setdefault("age", "18"))
# print(user.setdefault("sex", "male"))
# print(user)


# fromkeys() - создает словарь с заданными ключами и значениями
# dict.fromkeys(keys, value=None)

# keys = ['apple', 'banana', 'cherry']
#
# new_dict = dict.fromkeys(keys)
# print(new_dict)
#
# new_dict = dict.fromkeys(keys, 0)
# print(new_dict)


# copy() - создает копию словаря
# another_dict = user.copy()
# another_dict["age"] = 26
# print(user)
# print(another_dict)


# clear() - очищает словарь
print(user)
user.clear()
print(user)
