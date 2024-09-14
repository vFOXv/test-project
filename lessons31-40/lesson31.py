# Использование списковых включений (list comprehensions) - Решение практической части

products_list = [
    {"id": "1", "category": "smartphones", "is_top": True, "name": "iPhone 13", "price": 900, "quantity": 10},
    {"id": "2", "category": "laptops", "is_top": True, "name": "MacBook Air", "price": 1100, "quantity": 5},
    {"id": "3", "category": "smartphones", "is_top": False, "name": "Samsung Galaxy", "price": 700, "quantity": 15},
    {"id": "4", "category": "laptops", "is_top": False, "name": "HP Pavilion", "price": 800, "quantity": 7},
    {"id": "5", "category": "computers", "is_top": False, "name": "Dell Desktop", "price": 750, "quantity": 8},
    {"id": "6", "category": "computers", "is_top": True, "name": "Apple iMac", "price": 1500, "quantity": 4},
    {"id": "7", "category": "smartphones", "is_top": True, "name": "Google Pixel", "price": 800, "quantity": 3},
    {"id": "8", "category": "laptops", "is_top": False, "name": "Asus ZenBook", "price": 1050, "quantity": 6},
    {"id": "9", "category": "smartphones", "is_top": False, "name": "Xiaomi Mi 11", "price": 650, "quantity": 12},
    {"id": "10", "category": "laptops", "is_top": True, "name": "Lenovo ThinkPad", "price": 950, "quantity": 9},
    {"id": "11", "category": "computers", "is_top": False, "name": "HP Envy Desktop", "price": 900, "quantity": 11},
    {"id": "12", "category": "smartphones", "is_top": True, "name": "OnePlus 9", "price": 850, "quantity": 6},
    {"id": "13", "category": "laptops", "is_top": False, "name": "Dell XPS 13", "price": 1200, "quantity": 3},
    {"id": "14", "category": "computers", "is_top": True, "name": "Acer Aspire", "price": 1100, "quantity": 7},
    {"id": "15", "category": "smartphones", "is_top": False, "name": "Sony Xperia", "price": 750, "quantity": 5},
    {"id": "16", "category": "laptops", "is_top": False, "name": "Microsoft Surface Laptop", "price": 1300, "quantity": 2},
]

basket = {}
current_page = 1
selected_category = "smartphones"
search_query = ""

categories = [
    {"key": "smartphones", "name": "Смартфоны"},
    {"key": "laptops", "name": "Ноутбуки"},
    {"key": "computers", "name": "Компьютеры"},
]

while True:
    action = ""

    print("\n" + "-" * 50 + "\n")
    print(
        "1. Главная страница\n"
        "2. Страница категорий\n"
        "3. Страница поиска\n"
        "4. Страница корзины\n"
    )

    if current_page == 1:
        print("\nГлавная страница:\n")
        top_products = [product for product in products_list if product["is_top"]][:5]

        print("Топ-5 товаров:")
        for product in top_products:
            print(f"{product['id']}. {product['name']} - ${product['price']} ({product['quantity']} шт.)")

        print("\nДоступные команды:\n"
              " - mtp (переход на другую страницу)\n"
              " - atb (добавить товары в корзину)\n"
              " - exit (выйти из программы)\n")

        action = input("Выберите необходимое действие: ")

    elif current_page == 2:
        print("\nКатегории товаров:")
        for category in categories:
            print(f"{category['key']} - {category['name']}")

        print(f"\nТовары в категории {selected_category}:")
        category_products = [product for product in products_list if product["category"] == selected_category]
        for product in category_products:
            print(f"{product['id']}. {product['name']} - ${product['price']} ({product['quantity']} шт.)")

        print("\nДоступные команды:\n"
              " - mtp (переход на другую страницу)\n"
              " - atb (добавить товары в корзину)\n"
              " - sc (выбрать категорию)\n"
              " - exit (выйти из программы)\n")

        action = input("Выберите необходимое действие: ")

    elif current_page == 3:
        print("\nСтраница поиска:")
        if search_query.strip():
            print(f"Вы ищете: {search_query}")
            search_result = [product for product in products_list if search_query.lower() in product["name"].lower()]
        else:
            print("Вы ничего не ввели")
            search_result = products_list

        print(f"Результаты поиска:")
        for product in search_result:
            print(f"{product['id']}. {product['name']} - ${product['price']} ({product['quantity']} шт.)")

        print("\nДоступные команды:\n"
              " - mtp (переход на другую страницу)\n"
              " - atb (добавить товары в корзину)\n"
              " - s (поиск товаров)\n"
              " - exit (выйти из программы)\n")

        action = input("Выберите необходимое действие: ")

    elif current_page == 4:
        print("\nКорзина:")

        if len(basket.keys()) == 0:
            print("Корзина пуста")
        else:
            for product_id in basket.keys():
                print(f"{product_id}. {basket[product_id]['name']} - ${basket[product_id]['price']} ({basket[product_id]['quantity']} шт.)")

        buy_it = input("\nХотите ли вы преобрести выбранные товары? (y/n): ")

        if buy_it == "y":
            print("Спасибо за покупку!")
            for product in products_list:
                if product["id"] in basket.keys():
                    product["quantity"] -= basket[product["id"]]["quantity"]

            basket = {}
            current_page = 1
            continue

        print("\nДоступные команды:\n"
              " - mtp (переход на другую страницу)\n"
              " - exit (выйти из программы)\n")

        action = input("Выберите необходимое действие: ")

    else:
        print("Указанная страница не поддерживается.")
        continue

    if action == "mtp":
        target_page = input("Введите номер страницы: ")

        if target_page in ["1", "2", "3", "4"]:
            current_page = int(target_page)
            continue

    elif action == "atb":
        if current_page in [1, 2, 3]:
            product_ids_string = input("Введите через запятую id добавляемых в корзину товаров: ")
            product_ids = product_ids_string.split(",")
            products_to_add_to_basket = [{**product, "quantity": product_ids.count(product["id"])}
                                         for product in products_list
                                         if product["id"] in product_ids]

            for product in products_to_add_to_basket:
                if product["id"] in basket:
                    basket[product["id"]]["quantity"] += product["quantity"]
                else:
                    basket[product["id"]] = product
                    basket[product["id"]]["quantity"] = product["quantity"]

                print(f"Товар {product['name']} x {product['quantity']} шт. добавлен в корзину.")
        else:
            print("Текущая страница не поддерживает добавление в корзину.")

    elif action == "sc":
        if current_page == 2:
            category_id = input("Введите уникальный ключ категории: ")
            category_ids = [category["key"] for category in categories]

            if category_id in category_ids:
                selected_category = category_id
            else:
                print(f"Категория с таким ключом {category_id} не найдена.")
        else:
            print("Текущая страница не поддерживает выбор категории товаров.")

    elif action == "s":
        if current_page == 3:
            search_query = input("Введите поисковый запрос: ")
        else:
            print("Текущая страница не поддерживает поиск товаров.")

    elif action == "exit":
        print("Выход из программы.")
        break