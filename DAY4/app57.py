# Recap 
# python native types/class
# -----------------------------
# int float complex str bytes list tuple dict set <== type  - Class
#                             ====       ====
# user defined class - mutable 
# ------------------
# class <className>:
# -----  ==========
# |           |-> User defined Name 
# keyword
#
# using className - we can access class attributes
# ----------------  we can add,modify class attribute values
#                   using del() - we can delete class attribute 
# ===================================================================
class product:
    pid  = 101
    pname = 'demoA'

print(type(int),type(list),type(dict),type(bool),type(float))
print(type(product))

print(product.pid,product.pname)
#print(product.PID) # Vs NameError 
product.pname = 'Laptop' # we can modify an exiting value
#######
print(product.pname)
product.pcost = 10000 # adding new attribute to an existing class
print(product.pid,product.pname,product.pcost)
'''
>>> class product:
...     pid = 101
...
>>> product
<class '__main__.product'>
>>>
>>> product.pid
101
>>> product.pid = 200
>>> product.pid
200
>>> product.pid = 300
>>> product.pid = 300
>>> product.pid
300
>>> product.pid
300
>>> product()
<__main__.product object at 0x0000023DABDF38C0>
>>>
>>> product()
<__main__.product object at 0x0000023DAC289E50>
>>>
>>> obj1 = product()
>>> obj2 = product()
>>>
>>> obj1.pid
300
>>> obj2.pid
300
>>> product.pid = 505  ## using className
>>> product.pid
505
>>> obj1.pid
505
>>> obj2.pid
505
>>> obj1.pid = 'B-101' # object based initialization
>>> obj1.pid
'B-101'
>>>
>>> product.pid = 305
>>> obj1.pid
'B-101'
>>> obj2.pid
305
>>> obj2.pid = 'B-102' # object based initialization
>>> obj1.pid
'B-101'
>>> obj2.pid
'B-102'
>>>
>>> product.pid= 405
>>> #######
>>>
>>> obj1.pid
'B-101'
>>> obj2.pid
'B-102'
>>>
>>> obj3 = product()
>>> obj3.pid
405
>>>
'''
