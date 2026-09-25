def load_inventory():
    orders = []
    try:
        with open("inventory.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        order_id = int(parts[0].strip())
                        product_name = parts[1].strip()
                        quantity = int(parts[2].strip())
                        orders.append((order_id, product_name, quantity))
    except FileNotFoundError:
        pass

    return orders

history = load_inventory()

def display_inventory(orders):
    print("Current Orders:\n")
    for order in orders:
        print(f"{order[0]}, {order[1]}, {order[2]}")
    print()

product_name = input("Enter Product Name: ").strip()
quantity = int(input("Enter Quantity: ").strip())

next_id = 1001 + len(history)

new_order = f"{next_id},{product_name},{quantity}"
history.append(new_order)

print("\nNew Order Added:")
print(new_order)