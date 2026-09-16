records = ('p101,pA,1000',
           'p102,pB,2000',
           'p103,pC,3000',
           'p104,pD,4000')

# Iterate a records 
#  -> display produce name Uppercase chars
#  -> calculate sum of product cost
#  -> display total product cost at the end of the line
total_cost = 0

for record in records:
    product_id, product_name, product_cost = record.split(',')
    print(product_name.upper())
    total_cost += int(product_cost)

print(f'Total product cost: {total_cost}')
#-------------------------------------------------------

# ask -> llm - enumerate
# ask -> demonstrate - enumerate
for index,value in enumerate('python',1):
    print(f'{index} - {value}')
    
contents = ['data1','data2','data3','data4','data5','data6','data7']
for index,value in enumerate(contents,1):
    print(f'{index} - {value}')

