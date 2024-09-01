# Методы списков


# copy() - создает копию списка
# len() - возвращает количество элементов в списке

# append() - добавляет элемент в конец списка
# insert() - добавляет элемент в указанную позицию
# extend() - расширяет список, добавляя элементы из другого списка
# remove() - удаляет элемент из списка
# pop() - удаляет элемент из списка и возвращает его
# del - удаляет элемент из списка либо сам список

# clear() - очищает список
# index() - возвращает позицию элемента в списке
# count() - возвращает количество элементов в списке
# sort() - сортирует список
# reverse() - разворачивает список










# Копирование списков
# some_list = ["string", 0, True, [1, 2, 3]]
# other_list = some_list.copy()
# some_list[0] = "new string"
# print(some_list)
# print(other_list)


# Количество элементов в списке
# some_list = ["string", 0, True, [1, 2, 3]]
# print(len(some_list))


# Методы списков
# some_list = ["string", 0, True, [1, 2, 3]]
#
# some_list.append("new string")
# print(some_list)
#
# some_list.insert(0, "new string")
# print(some_list)
#
# some_list.extend([4, 5, 6])
# print(some_list)
#
# some_list.remove("new string")
# print(some_list)
#
# removed_element = some_list.pop()
# print(removed_element)
# print(some_list)
#
# removed_element = some_list.pop(0)
# print(removed_element)
# print(some_list)
#
# del some_list[1]
# print(some_list)
#
# del some_list
# print(some_list)


# Очистка списка
# some_list = ["string", 0, True, [1, 2, 3]]
# print(some_list)
# some_list.clear()
# print(some_list)


# Поиск элемента в списке
# some_list = ["string", 0, True, [1, 2, 3]]
# print(some_list.index("string"))
# print(some_list.index("new string"))


# Подсчет количества элементов в списке
# some_list = ["string", 0, True, [1, 2, 3], "string"]
# print(some_list.count("string"))


# Сортировка списков
# some_list = ["asd", "sdfsdf", "rtytry", "ertert"]
# some_list.sort()
# print(some_list)
# some_list.sort(reverse=True)
# print(some_list)


# Разворот списка
some_list = ["string", 0, True, [1, 2, 3]]
some_list.reverse()
print(some_list)

