# Работа с файлами - Запись данных в файлы .txt - Решение практической части


# Функция записи информации о товаре в отчет
def write_report(product, quantity, price):
    with open('sales_report.txt', 'a', encoding='utf-8') as file:
        file.write(f'Название товара: {product}, '
                   f'Количество: {quantity}, '
                   f'Цена: {price}, '
                   f'Сумма: {quantity * price}\n')


# Функция для логирования ошибок
def log_error(error_message):
    with open('error_log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{error_message}\n')


# Основная программа
while True:
    try:
        product = input('Введите название товара (или "стоп" для завершения): ')

        if product == 'стоп':
            break

        if not product.strip():
            raise ValueError(f'Неправильное название товара - {product}')

        quantity = input('Введите количество: ')

        if not quantity.isdigit() or int(quantity) <= 0:
            raise ValueError(f'Некорректное количество товара "{product}" - {quantity}')

        price = input('Введите цену: ')

        if not price.isdigit() or int(price) <= 0:
            raise ValueError(f'Некорректная цена товара "{product}" - {price}')

        quantity = int(quantity)
        price = int(price)
        write_report(product, quantity, price)

        print('')
    except ValueError as error:
        error_string = f'Ошибка: {error}'
        log_error(error_string)
        print(f'{error_string}\n')