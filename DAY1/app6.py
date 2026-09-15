# Keyboard -------- PythonCode ------------ Monitor
#           input()              print()
#
#  variable = input('user defined message')
#  ---------                             
#    |->default data type is string
n = input('Enter n value:')
print(f'n value is:{n} and type of n is:{type(n)}')
total = int(n) + 100 
print(f'total value is:{total}')
print(n+str(100)) # <== '45'+'100' = '45100' 