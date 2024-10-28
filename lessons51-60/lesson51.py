import json

items = [
    {
        "name": "Смартфон",
        "price": 35000,
        "category": "Электроника",
        "in_stock": True,
        "sku": "SM12345"
    },
    {
        "name": "Ноутбук",
        "price": 55000,
        "category": "Электроника",
        "in_stock": True,
        "sku": "NB12345"
    },
    {
        "name": "Телевизор",
        "price": 25000,
        "category": "Электроника",
        "in_stock": False,
        "sku": "TV12345"
    },
    {
        "name": "Компьютер",
        "price": None,
        "category": "Электроника",
        "in_stock": True,
        "sku": "CP12345"
    },
    {
        "name": "Холодильник",
        "price": 20000,
        "category": "Бытовая техника",
        "in_stock": True,
        "sku": "RF12345"
    }
]


with open("catalog.json", "w", encoding="utf-8") as file:
    json.dump(items, file, indent=4, ensure_ascii=False)