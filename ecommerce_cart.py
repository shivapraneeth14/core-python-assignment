def calculate_total_price(cart_items):
    
    if not cart_items:
        return 0

    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total *= 0.9  # 10% discount

    return total

cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}

total_price = calculate_total_price(cart_items)
print(f"Total Price: {int(total_price)}")
