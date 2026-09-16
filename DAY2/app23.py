'''
Given List
Emp = ['101,raj,sales,1000','102,leo,prod,2000','103,shiv,sales,3000','104,ram,admin,4000']
Iterate the given list - step by step
using membership operator filter sales dept
split each string(line) into multiple values(list)based on sep(,)
| 
display Emp name - working dept at the end display sum of emp's cost
                                                  ================
'''
Emp = ['101,raj,sales,1000','102,leo,prod,2000',
       '103,shiv,sales,3000','104,ram,admin,4000']

print('-'*35)
total = 0
for var in Emp:
    if 'sales' in var:
        eid,ename,edept,ecost = var.split(",")
        print(f'Emp name is:{ename.title()}\t Dept is:{edept.lower()}')
        total = total + int(ecost)
else:
    print('-'*35)
    print(f'Sum of sales dept emp cost is:{total}')
    print('-'*35)
    