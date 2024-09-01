# Списки


# Инициализация списка
# some_list = ["string", 0, True, [1, 2, 3]]
# another_list = list("ABCD")
#
# print(some_list)
# print(another_list)


# Доступ к элементам списка
# print(some_list[0])
# print(some_list[1])
# print(some_list[-2])
# print(some_list[-1])


# Срезы списков
# Синтаксис срезов списков: [start:stop:step]
# some_list = ["string", 0, True, [1, 2, 3]]
# print(some_list[-2::-1])


# Изменение элементов списка
# some_list = ["string", 0, True, [1, 2, 3]]
# print(some_list)
# some_list[0] = "new string"
# some_list[1] = 1
# some_list[2] = False
# some_list[3] = [4, 5, 6]
# print(some_list)


# Ссылочный тип данных
# some_list = ["string", 0, True, [1, 2, 3]]
# other_list = some_list
# some_list[0] = "new string"
# other_list[1] = 1
# print(some_list)
# print(other_list)


# Копирование списков
some_list = ["string", 0, True, [1, 2, 3]]
# other_list = some_list.copy()
# some_list[0] = "new string"
# print(some_list)
# print(other_list)


# Проверка существования элемента в списке
# some_list = ["string", 0, True, [1, 2, 3]]
# print("string" in some_list)
# print("new string" in some_list)


# Итерация по списку
some_list = ["string", 0, True, [1, 2, 3]]
for item in some_list:
    print(item)

