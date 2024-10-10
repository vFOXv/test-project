# * Работа с файлами - Чтение данных из .txt файлов


# ? Пример 1: Чтение всего содержимого файла
with open('lesson47_example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)


# ? Пример 2: Чтение файла построчно
with open('lesson47_large_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        cropped_line = line.strip() # Отбрасываем пробелы и переносы строки
        if cropped_line:
            print(cropped_line)


# ? Пример 3: Чтение одной строки с использованием readline()

# Чтение первой строки
with open('lesson47_example.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    print("Первая строка:", first_line)

# Чтение первых 5 строк
with open('lesson47_example.txt', 'r', encoding='utf-8') as file:
    file.readline()  # Пропускаем первую строку

    for i in range(5):
        line = file.readline()
        print(line.strip())

# Пропускаем пустые строки
with open('lesson47_example.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if line.strip():
            print(line.strip())


# ? Пример 4: Чтение всех строк как списка с использованием readlines()
with open('lesson47_example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print("Все строки файла:")
    for line in lines:
        print(line.strip())


# ? Пример 5: Чтение части файла с использованием read(size)
with open('lesson47_large_file.txt', 'r', encoding='utf-8') as file:
    while True:
        chunk = file.read(1024)  # Чтение по 1024 символа
        if not chunk:
            break
        print(chunk)
