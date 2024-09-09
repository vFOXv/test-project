# Методы множеств


# add() - добавляет элемент в множество
# remove() - удаляет элемент из множества
# discard() - удаляет элемент из множества, если он присутствует
# clear() - очищает множество
# copy() - создает копию множества
# union() - объединяет множества
# intersection() - возвращает пересечение множеств
# intersection_update() - оставляет в множестве только элементы, присутствующие в обоих множествах
# difference() - возвращает разность множеств
# difference_update() - обновляет множество, удаляя все элементы, присутствующие в обоих множествах
# symmetric_difference() - возвращает симметрическую разность множеств
# symmetric_difference_update() - обновляет множество, удаляя все элементы, присутствующие в обоих множествах
# issubset() - возвращает True, если все элементы первого множества присутствуют во втором множестве
# issuperset() - возвращает True, если все элементы второго множества присутствуют в первом множестве
# isdisjoint() - возвращает True, если множества не имеют общих элементов


# Добавление элемента в множество

# some_set = {1, 2, 3}
# some_set.add(4)
# print(some_set)


# Удаление элемента из множества

# some_set = {1, 2, 3}
# some_set.remove(2)
# print(some_set)


# Удаление элемента из множества, если он присутствует

# some_set = {1, 2, 3}
# some_set.discard(4)
# print(some_set)


# Очистка множества

# some_set = {1, 2, 3}
# some_set.clear()
# print(some_set)


# Копирование множества

# some_set = {1, 2, 3}
# some_set_copy = some_set.copy()
# some_set_copy.add(4)
# print(some_set)
# print(some_set_copy)


# Объединение множеств

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# some_set.update(some_other_set)
# print(some_set)
# print(some_other_set)


# Пересечение множеств

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# print(some_set.intersection(some_other_set))
# print(some_set)
# print(some_other_set)


# Сохранение в множестве только элементов, присутствующие в обоих множествах

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# some_set.intersection_update(some_other_set)
# print(some_set)
# print(some_other_set)


# Разность множеств

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# print(some_set.difference(some_other_set))
# print(some_other_set.difference(some_set))
# print(some_set)
# print(some_other_set)


# Сохранение в множестве только элементов, присутствующих только в первом множестве

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# some_set.difference_update(some_other_set)
# print(some_set)


# Симметрическая разность множеств

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# print(some_set.symmetric_difference(some_other_set))
# print(some_other_set.symmetric_difference(some_set))


# Сохранение во множестве уникальных элементов из двух сравниваемых множеств

# some_set = {1, 2, 3}
# some_other_set = {3, 4, 5}
# some_set.symmetric_difference_update(some_other_set)
# print(some_set)
# print(some_other_set)


# Проверка второго множества на принадлежность первому множеству

# some_set = {1, 2, 3, 4, 5}
# some_other_set = {3, 4, 6}
# print(some_other_set.issubset(some_set))


# Проверка содержит ли первое множество второе множество

# some_set = {1, 2, 3, 4, 5}
# some_other_set = {3, 4, 5}
# print(some_set.issuperset(some_other_set))


# Проверка полного отличия множеств

some_set = {1, 2}
some_other_set = {3, 4, 5}
print(some_set.isdisjoint(some_other_set))
