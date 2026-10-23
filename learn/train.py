products = [
    {"name": "shoes", "price": 40},
    {"name": "hat", "price": 12},
    {"name": "bag", "price": 25},
    {"name": "jacket", "price": 50},
    {"name": "pants", "price": 30},
    {"name": "shirt", "price": 20},
    {"name": "socks", "price": 5},
    {"name": "scarf", "price": 10},
    {"name": "gloves", "price": 15},
    {"name": "cap", "price": 8},
    {"name": "umbrella", "price": 12},
    {"name": "raincoat", "price": 35},
    {"name": "umbrella", "price": 12},
]
order = []

def show_products():
    number = 1
    for product in products:
        print(f"{number}. {product['name']} costs {product['price']}")
        number = number + 1

def add_to_order():
    show_products()
    try:
        choice = int(input("Product number:"))
        if choice < 1 or choice > len(products):
            print("That product does not exist")
            return
        product = products[choice - 1]
        order.append(product)
        print(f"Added {product['name']}")
        print(order)
    except ValueError:
        print("Please type a number")

def show_total():
    total = 0
    for product in order:
        total = total + product['price']
        print(product["name"])
    print(f"Total is {total}")

while True:
    print("1. See products")
    print("2. Add to order")
    print("3. Show total")
    print("4. Quit")
    command = input("Choose: ").strip()

    if command == "1":
        show_products()
    elif command == "2":
        add_to_order()
    elif command == "3":
        show_total()
    elif command == "4":
        print("Goodbye!")
        break
    else:
        print("Unknown command")

        
