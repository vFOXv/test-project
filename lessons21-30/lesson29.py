products_list = {}

while True:
    print("\n" + "-" * 50 + "\n")
    print(
        "1. Добавить новый товар\n"
        "2. Удалить существующий\n"
        "3. Изменить существующий\n"
        "4. Показать список\n"
        "5. Выход\n"
    )

    choice = input("Выберите необходимое действие: ")
    print("")

    if choice == "1":
        print("Добавить новый товар\n")
        key = input("Введите уникальный ключ: ")

        if key in products_list:
            print("Такой ключ уже существует")
            continue

        title = input("Введите название: ")
        price = float(input("Введите цену: "))
        unit = input("Введите единицу измерения (кг, шт, л): ")
        quantity = float(input("Введите количество: "))

        products_list[key] = {
            "title": title,
            "price": price,
            "unit": unit,
            "quantity": quantity
        }

        print(f"\nТовар {title} добавлен")
    elif choice == "2":
        print("Удалить товар\n")
        key = input("Введите ключ товара, который необходимо удалить: ")

        if not key in products_list:
            print("Товара с таким ключом не существует")
            continue

        removed_product = products_list.pop(key)

        print(f"\nТовар {removed_product['title']} удален")
    elif choice == "3":
        print("Изменить товар\n")
        key = input("Введите ключ товара, который необходимо изменить: ")

        if not key in products_list:
            print("Товара с таким ключом не существует")
            continue

        product = products_list[key]

        title = input(f"Введите название ({product["title"]}): ") or product["title"]
        price = input(f"Введите цену ({product["price"]}): ") or product["price"]
        unit = input(f"Введите единицу измерения (кг, шт, л) ({product["unit"]}): ") or product["unit"]
        quantity = input(f"Введите количество ({product["quantity"]}): ") or product["quantity"]

        products_list[key] = {
            "title": title,
            "price": float(price),
            "unit": unit,
            "quantity": float(quantity),
        }

        print(f"\nТовар с ключом {key} изменен")
    elif choice == "4":
        if not products_list:
            print("Список пуст")
            continue

        for index, (key, product) in enumerate(products_list.items(), start=1):
            print(f"{index}. {key} - {product['title']} (${product['price']}) х {product['quantity']} {product['unit']}")
    elif choice == "5":
        print("Выход из программы")
        break
    else:
        print("Такого действия нет")
