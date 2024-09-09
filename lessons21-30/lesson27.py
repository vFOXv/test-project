# Dictionaries (словари)


# Словари - упорядоченные коллекции произвольных объектов с доступом по ключу
# Если после добавления "ключей: значений" в словарь перебрать их,
# то они будут в том же порядке, в котором были добавлены в него.


# Синтаксис словарей

# some_dict = {"key": "value", "key2": "value2"}
# another_dict = dict(key="value", key2="value2")


# Создание пустого словаря

# some_dict = {}
# another_dict = dict()
#
# print(some_dict)
# print(another_dict)


# Создание словаря из пар ключ-значение

some_dict = {
    "key": "value",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}
another_dict = dict(key="value", key2="value2")

print(some_dict)
print(another_dict)
