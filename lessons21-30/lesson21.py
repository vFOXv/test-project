# Функции range и enumerate


# Когда использовать range():
# 1. Когда нужно выполнить цикл фиксированное количество раз.
# 2. Когда требуется создать диапазон чисел с определённым шагом.
# 3. Когда нужен обратный порядок итерации.

# range(start, stop, step)
# start - начало диапазона (0 по умолчанию)
# stop - конец диапазона
# step - шаг (1 по умолчанию)

print(list(range(5)))
print(list(range(2, 5)))
print(list(range(2, 5, 2)))


# Пример итерации по списку через range

print("Введите 5 последних прочитанных вами книг")
books = []

for i in range(5):
    book = input("Введите название книги: ")
    books.append(book)

print(books)

for i in range(5, 0, -1):
    print(books[i - 1])


# Когда использовать enumerate():
# 1. Когда нужно одновременно работать с элементами и их индексами.
# 2. Когда требуется номеровать элементы при итерации, начиная с определённого числа.

# enumerate(iterable, start=0)
# iterable - итерируемый объект
# start - начальное значение индекса


products = ["Молоко", "Сыр", "Мясо"]

print(list(enumerate(products)))

for i, product in enumerate(products):
    print(f"{i + 1}. {product}")