import json  # Импортируем модуль json

# * Формат JSON — Запись данных в файл .json


# ? Пример 1. Запись данных в файл в формате JSON

# Метод json.dump() используется для записи данных в файл.

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)


# ? Пример 2. Запись данных в файл в формате JSON в более удобном виде

# indent=4 — делает JSON-файл более читаемым, добавляя отступы.

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)


# ? Пример 3. Работа с русскими символами и параметр ensure_ascii

# ensure_ascii=False — сохраняет данные на языках
# отличных от английского корректно.

data = {
    "name": "Иван",
    "age": 30,
    "city": "Москва"
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


# ? Пример 4. Разница между записью в файл и преобразованием в строку

# Метод json.dumps() используется для
# преобразования данных в строку в формате JSON.

data = {
    "name": "Иван",
    "age": 30,
    "city": "Москва"
}

json_string = json.dumps(data, ensure_ascii=False, indent=4)
print(json_string)