# Работа с файлами - Кодировка файлов


# Открытие .txt файла
with open('lesson44_example.txt', 'r', encoding='windows-1251') as file:
    content = file.read()
    print(content)


# Изменение кодировки текста
with open('lesson44_example.txt', 'r', encoding='windows-1251') as file:
    content = file.read()

with open('lesson44_example_utf8.txt', 'w', encoding='utf-8') as file:
    file.write(content)

print("Файл успешно перекодирован в UTF-8")


import csv

# # Открытие CSV файла
with open('lesson44_example.csv', encoding='windows-1251') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

