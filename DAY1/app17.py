prod_name = "Laptop"
prod_cost = 50000.45
no_qty = 5
prod_status = True
#################################
prod_info = ["Laptop",50000.45,5,True] ## List 
print(type(prod_info))
print(len(prod_info))
print(prod_info)
print(prod_info[0])
print(prod_info[-1])
print(prod_info[-3:]) # last 3 values
if 'Laptop' in prod_info:
    print('Yes Product is found')
    print(f'{prod_info[0]} cost is:{prod_info[-3]}')
else:
    print('Sorry product is not found')

# listname[oldIndex] = updated
prod_info[-3] = "60000.23 INR" # modification

print("Updated Product details:-")
print(prod_info)
