from models import Product, Customer

def process_line(line, products, customers):
    parts = line.strip().split()
    if not parts:
        return

    command = parts[0]

    if command == "register":
        name = parts[1]
        price = float(parts[2].replace('$', ''))
        products[name] = Product(name, price)

    elif command == "checkin":
        name = parts[1]
        quantity = int(parts[2])
        if name in products:
            products[name].stock += quantity

    elif command == "order":
        customer_name = parts[1]
        product_name = parts[2]
        quantity = int(parts[3])

        if product_name not in products:
            return

        product = products[product_name]
        if product.stock < quantity:
            return

        if customer_name not in customers:
            customers[customer_name] = Customer(customer_name)

        customers[customer_name].add_order(product_name, quantity, product.price)
        product.stock -= quantity
