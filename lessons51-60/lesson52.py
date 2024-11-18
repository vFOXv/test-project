import json  # Импортируем модуль json

# * Формат JSON — Чтение данных формата .json

# Для чтения данных в формате JSON используются 2 метода:
# json.load() - Чтение данных из JSON-файла
# json.loads() - Чтение данных из строки


# ? Пример 1. Чтение JSON-файла

with open('lesson52_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

for person in data:
    print(f'{person["name"]} живет в городе {person["city"]}.')


# # ? Пример 2. Чтение строки в формате JSON
#
# json_string = '[{"name": "Саймон", "age": 25, "city": "Нью-Йорк"}, {"name": "Алиса", "age": 30, "city": "Лондон"}]'
# data = json.loads(json_string)
# print(data)
#
# for person in data:
#     print(f'{person["name"]} живет в городе {person["city"]}.')
