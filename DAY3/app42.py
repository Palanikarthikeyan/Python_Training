

def display(cus_name='Guest', cus_ID=0, *args, **kwargs):
    '''display customer details with default, variable-length, and keyword arguments'''
    print(f'Customer name:{cus_name} ID:{cus_ID}')
    if args:
        print('Extra positional arguments:', args)
    if kwargs:
        print('Keyword arguments:', kwargs)

# Example calls
print('Default call:')
display()
print('\nNormal call:')
display('Alice', 101)
print('\nVariable-length positional arguments:')
display('Alice', 101, 'VIP', 'Premium')
print('\nKeyword arguments:')

display(cus_name='Bob', cus_ID=202, city='Chennai', status='Active')