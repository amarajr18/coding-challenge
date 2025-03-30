def generate_report(customers):
    for customer in sorted(customers.values(), key=lambda c: c.name):
        print(customer.get_summary())
