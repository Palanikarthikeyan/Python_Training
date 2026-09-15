# for loop - collection based iteration
#            ----------
# for variable in <collection>:
#     # code block
# for in - keywords
#---------------------------------
for var in 'python':
    print(f'var value is:{var}')
    print('-'*10)

# Task:
# s='123456789'
# Calculate sum of the digits from given string
#          ==================
s='123456789'
total = 0
for var in s:
    total = total + int(var)
else:
    print(f' Sum of {s} is {total}')