import time

def display(cus_name,cus_ID): ## Requirement arguments
    '''display customer details'''
    print(f'Customer name:{cus_name} ID:{cus_ID}')
    
print('Main-Entry-(1)')
# display() # Error
# display('cusA') # Error  
# display('cusA',123,'data') # Error

display('cusA','C-123') # 1st call
time.sleep(2)
display('cusB','C-332') # 2nd call 
time.sleep(2)
display('cusC','C-344') # 3rd call

### default args - example
def product_info(pname='Antenna',pID='CW91'): # default arguments
    '''product info'''
    print(f'Product Name:{pname} ID:{pID}')
    
product_info()
product_info('wirelessLAN')
product_info('Switch','S124')