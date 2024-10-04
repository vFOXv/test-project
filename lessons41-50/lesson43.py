# Область видимости переменных


# Области видимости переменных
# - Локальная область видимости
# - Глобальная область видимости
# - Нелокальная область видимости


# Локальная область видимости
def calculate_total(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return total


final_price = calculate_total(100, 0.2)
print(f"Итоговая сумма: {final_price}")


# Глобальная область видимости
log_entries = []


def add_log_entry(entry):
    """Добавляет запись в глобальный список log_entries без использования global."""
    log_entries.append(entry)


def print_log():
    """Печатает все записи в журнале."""
    for i, entry in enumerate(log_entries, 1):
        print(f"{i}. {entry}")


add_log_entry("Программа запущена.")
add_log_entry("Обработка данных завершена.")
add_log_entry("Программа завершена.")

print_log()


call_count = 0


def process_data(data):
    global call_count
    call_count += 1
    print(f"Обработка данных... (Вызов #{call_count})")
    # Симуляция обработки данных
    processed_data = data.upper()
    return processed_data


print(process_data("пример"))
print(process_data("ещё пример"))
print(process_data("ещё один пример"))

print(f"Функция была вызвана {call_count} раз(а).")


# Нелокальная область видимости + замыкание
def cache_factorial():
    cache = {}
    call_count = 0

    def factorial(n):
        nonlocal call_count
        call_count += 1
        print(f"Вызов #{call_count}")

        if n in cache:
            print(f"Берем из кэша: {n}! = {cache[n]}")
            return cache[n]

        result = 1
        for i in range(2, n + 1):
            result *= i

        cache[n] = result
        print(f"Вычисляем и сохраняем: {n}! = {result}")
        return result

    return factorial


cached_factorial = cache_factorial()

cached_factorial(5)
cached_factorial(3)
cached_factorial(5)
cached_factorial(4)
cached_factorial(3)

