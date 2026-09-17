'''
d = {'K1':'V1','K2':'V2'}

To fetch/get single data from given dict
dictName['OldKey'] ->Value/KeyError
 <or>
dictName.get('oldKey',defaultValue) -> Value / None 

'''
products = {'pid':'p101','device':'switch','vendor':'cisco'}
print(products.get('pid')) # print(products['pid'])
print(products.get('device')) # print(products['device'])
print(products.get('Vendor','CISCO')) # print(products['Vendor']) # KeyError ->Exit

for var in products:
    print(f'{var} - {products[var]}')
else:
    print(f'Total no.of items:{len(products)}')