# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

def process_orders(orders):
    for order in orders:
        # Unpacking the tuple into variables
        customer_name, product, quantity = order
        # Formatting the order details
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")
# Given sample data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]
# Calls the function with the sample data
process_orders(orders) 