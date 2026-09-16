products = [
    ['P1', ('Laptop',) ,75000],
    ['P2', ('Mobile Phone',), 25000],
    ['P3', ('Headphones',), 3000],
    ['P4', ('Keyboard',), 1500],
]

for product in products:
    print(f'ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')
