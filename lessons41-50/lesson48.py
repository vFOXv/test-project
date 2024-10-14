# Работа с файлами - Чтение данных из .txt файлов - Решение практической части


# Задание #1: Анализ лог-файлов
with open("lesson47_large_log_file.txt", "r", encoding="utf-8") as file:
    while True:
        line = file.readline()
        if not line:
            break
        if "ERROR" in line:
            print(line.strip())

# Задание #2: Чтение и форматирование контактов
with open("lesson47_contacts.txt", "r", encoding="utf-8") as file:
    with open("formatted_contacts.txt", "w", encoding="utf-8") as output_file:
        for line in file:
            contact_parts = line.split(",")
            formatted_line = (f"{contact_parts[1].strip()} "
                              f"{contact_parts[0].strip()}: "
                              f"{contact_parts[2].strip()}\n")
            output_file.write(formatted_line)
            print(formatted_line.strip())


# output_lines = []
#
# with open("lesson47_contacts.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         contact_parts = line.split(",")
#         formatted_line = (f"{contact_parts[1].strip()} "
#                           f"{contact_parts[0].strip()}: "
#                           f"{contact_parts[2].strip()}\n")
#         output_lines.append(formatted_line)
#
# with open("formatted_contacts.txt", "w", encoding="utf-8") as output_file:
#     for line in output_lines:
#         output_file.write(line)
#         print(line.strip())