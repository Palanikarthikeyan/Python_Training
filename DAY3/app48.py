fobj = open(r'C:\\users\karth\emp.csv','r')
s1 = fobj.read()
fobj.close()
############# 
# another way
# --------------

with open(r'c:\\users\\karth\emp.csv','r') as fobj:
    s2 = fobj.read()

# fobj.close() - is not required 
# =============
    
print(s1)
print('')
print(s2)