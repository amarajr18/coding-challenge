class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []  # List of (product, quantity, total_price)

    def add_order(self, product_name, quantity, price_per_item):
        total = price_per_item * quantity
        self.orders.append((product_name, quantity, total))

    def get_summary(self):
        if not self.orders:
            return f"{self.name.capitalize()}: n/a"
        
        product_lines = []
        total_spent = 0

        for product, quantity, total in self.orders:
            product_lines.append(f"{product} - ${total:.2f}")
            total_spent += total

        avg_order_value = total_spent / len(self.orders)
        return f"{self.name.capitalize()}: {', '.join(product_lines)} | Average Order Value: ${avg_order_value:.2f}"
