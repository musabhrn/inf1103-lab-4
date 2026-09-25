def load_inventory():
    orders = []
    try:
        with open("inventory.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    orders.append(line)
    except FileNotFoundError:
        pass

    return orders

def save_inventory(orders):
    with open("inventory.txt", "w") as f:
        for order in orders:
            f.write(f"{order}\n")

def display_inventory(orders):
    print("Current Orders:\n")
    for order in orders:
        parts = order.split(",")
        if len(parts) == 3:
            print(f"{parts[0].strip()}, {parts[1].strip()}, {parts[2].strip()}")
    print()

history = load_inventory()

display_inventory(history)

product_name = input("Enter Product Name: ").strip()
quantity = int(input("Enter Quantity: ").strip())

next_id = 1001 + len(history)

new_order = f"{next_id},{product_name},{quantity}"
history.append(new_order)

print("\nNew Order Added:")
print(new_order)
print()

save_inventory(history)
print("Order successfully saved to orders.txt")