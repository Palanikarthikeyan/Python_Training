def display():
    '''display customer records'''
    cus_name = 'Raj'
    cus_id = 'C-123'
    print(f'Customer name:{cus_name} ID:{cus_id}')

def productInfo():
    '''this product info'''
    prod_name = 'Switch'
    prod_ID = 'S123'
    print(f'Product details:- {prod_name} and {prod_ID}')
    
print('This is main entry point-(1)')
display() # simple functioncall
print('') # empty line
productInfo() # simple function call
print('Exit from main block')