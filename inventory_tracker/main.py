import sys
from parser import process_line
from report import generate_report

def main(filename):
    products = {}
    customers = {}

    with open(filename, 'r') as file:
        for line in file:
            process_line(line, products, customers)

    generate_report(customers)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py input.txt")
    else:
        main(sys.argv[1])
