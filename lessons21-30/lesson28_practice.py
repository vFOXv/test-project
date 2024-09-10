# Методы словарей - Практика


# Задание
# Напишите программу для учёта ассортимента товаров, их количества и цен в магазине.
#
# При запуске программы и после выполнения любой операции выводите список доступных операций:
# 1. "Добавить новый товар",
# 2. "Удалить существующий",
# 3. "Изменить существующий",
# 4. "Показать список",
# 5. "Выход"
#
# Каждый товар имеет:
#  - уникальный ключ, например, "golden_apple";
#  - название;
#  - цену;
#  - единицу измерения (одна из перечисленных: "кг", "шт", "л")
#  - количество.
#
# Товары должны сохраняться в словарь с доступом по уникальному ключу
# и значением в виде словаря с остальными 4 полями (название, цена, единица измерения, количество).
#
# 1. При добавлении товару нужно поочереди запрашивать эти 5 полей:
# уникальный ключ, название, цену, единицу измерения и количество.
# Затем добавлять товар в словарь.
#
# 2. Удаление происходит по ключу.
#
# 3. Изменение происходит по ключу:
# - изменение названия;
# - изменение цены;
# - изменение количества.
# Если значение не передано, то оно не меняется.
#
# 4. Команда "Показать список" выводит список всех товаров в таком формате:
# 1. <key> - <title> ($<price>) х <quantity> <unit>
# Например:
# golden_apple - Golden Apple ($100) х 10 кг
#
# После каждого успешно выполненного действия, перед списком доступных операций выводите разделяющую линию:
# --------------------------------------------------


# Пример работы программы:

# --------------------------------------------------
#
# 1. "Добавить новый товар",
# 2. "Удалить существующий",
# 3. "Изменить существующий",
# 4. "Показать список",
# 5. "Выход"
#
# Выберите действие: 1
#
# Введите уникальный ключ: golden_apple
# Введите название: Golden Apple
# Введите цену: 100
# Введите единицу измерения: кг
# Введите количество: 10
#
# Товар добавлен в словарь
#
# --------------------------------------------------
#
# 1. "Добавить новый товар",
# 2. "Удалить существующий",
# 3. "Изменить существующий",
# 4. "Показать список",
# 5. "Выход"
#
# Выберите действие: 3
#
# Введите уникальный ключ: golden_apple
#
# Введите название:
# Введите цену: 95
# Введите единицу измерения:
# Введите количество: 10
#
# Товар изменен в словаре
#
# --------------------------------------------------
#
# 1. "Добавить новый товар",
# 2. "Удалить существующий",
# 3. "Изменить существующий",
# 4. "Показать список",
# 5. "Выход"


# Темы:
# - Приведение типов (lesson6)
# - Функции input и print (lesson10)
# - Условные операторы - if-else (lesson16)
# - Цикл while (lesson23)
# - Словари (lesson27)
# - Методы словарей (lesson28)


# Ваше решение:

