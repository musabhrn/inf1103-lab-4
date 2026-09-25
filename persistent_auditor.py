def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

        if user_input.lower() == "quit":
            return "quit"

        if not user_input.isdigit():
            print("Error. Invalid input. Please enter a non-negative number.")
            return None
        else:
            return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
     return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("-------------------------------")
    print(f"Total Deliveries Processed: {total_units}")    
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

 # Main
inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, result)

    if inventory > 500:
        print("Alert! Inventory total exceeds 500 units.")
        break

    tax = calculate_tax(result)
    deliveries_processed += 1

    print(f"Delivery added: {result} units | Tax on this delivery: {tax:.2f}")
    print(f"Running total inventory: {inventory}")

generate_report(deliveries_processed, failed_entries)