'''
How to add new data to an existing dict?
dictName['newKey'] = value
<or>
dictName.setdefault('newKey',Value)
dictName.setdefault('newKey') -> default value is None
'''
products = {'pid':'p101','device':'switch','vendor':'cisco'}
products.setdefault('config','network.cfg') 
print(products)
products.setdefault('K1')
print(products)
