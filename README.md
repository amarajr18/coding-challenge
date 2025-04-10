# coding-challenge
## Inventory Tracker

## The goal of this project was to build a simple inventory and customer order tracking system that:

1. Registers new products.

2. Tracks stock availability.

3. Allows customers to place orders.

4. Generates a summary report of customer purchases and average order value.

It outputs how much each customer spent and their average order value.

### Approach
I used Python with object-oriented design:
- `Product` tracks price and stock
- `Customer` stores individual orders
- A command parser handles each input type

Data structures are optimized for fast lookup using dictionaries.


### Thought Process
1. Broke the problem into components — product registration, stock updates, order processing, and reporting.

2. Modeled real-world entities using classes to mirror inventory and customer behavior.

3. Separated concerns by placing logic in distinct files/modules.

4. Used clean, idiomatic Python to make the code easy to understand and extend.

5. Focused on maintainability and future-proofing by applying best practices early.
.
.
.
.



Why Python?
Python was chosen for this project due to its:

Readable syntax, ideal for modeling real-world entities like Product and Customer

Quick development cycle, which supports rapid prototyping and iteration

Strong standard library, allowing file I/O and string handling without third-party packages

Community support, making it a great language for collaboration and learning

Python’s object-oriented nature also made it easier to build a modular and maintainable system.
.
.
.
.




Software Design & Structure
The code is organized using object-oriented principles and a modular architecture:

 models.py

Product: Represents an item with a name, price, and stock level.

Customer: Represents a buyer with an order history. Methods include:

add_order() to log purchases

get_summary() to format customer report output
......

parser.py
Contains the process_line() function to interpret and execute input commands (register, checkin, order).

Updates product inventory and customer records.
......

report.py
Responsible for generating final customer reports by sorting and formatting output from customer data.
.......

main.py
Entry point of the program.

Reads input file line-by-line and delegates processing to parser.py.

Calls the report generator once all commands are processed.
......



### Running
```bash
python main.py input.txt

### Here's my final structure with explanation to give clarity
inventory_tracker/
├── main.py              # handles CLI + orchestration
├── models.py            # contains Product and Customer classes
├── parser.py            # handles line-by-line command parsing
├── report.py            # handles generating + printing customer summaries
├── input.txt
├── README.md
└── tests/
    ├── __init__.py
    └── test_main.py
 Dockerfile                 # containerize temporarily and test it locally 


# to test the code I ran ( test locally on computer )
python -m unittest discover

# expected ouput 
Dan: n/a
Kate: hats - $410.00, socks - $34.50 | Average Order Value: $222.25

# Notes 
Invalid or unfulfillable orders are skipped.

Clean formatting and separation of logic make it extensible.