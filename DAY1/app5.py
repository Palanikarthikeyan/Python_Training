# typecasting
# --------------
n = 15
print(n)
print(type(n)) 
# int float str bool bytes list tuple set dict - class
# 10  10.0  'abc' True b'abc'  ... - object
print(type(10.0))
print(type('10.0'))

print(float(n)) # int to float
str(n) # int to str
n = str(n)
print(f"n value is:{n} and type of n is:{type(n)}") # int to str
v = '45'