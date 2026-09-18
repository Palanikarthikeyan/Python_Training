'''
Python program
===============
1. Procedure style code - block style - direct approach -- Understand python syntax + examples + logicalskills

2. Functional style code - Single line code <or> Expression style code 
                         - This is not block style code
                         - Computing/calculation 
                         - Highorder program ->  function1(anotherfunction)

3. OOP style - block style - <class - object>
#                           --------------------
#                                |-> object approach 
#                          - Application developement 
'''
def f1(a):
    return a + 100
L = [] # empty list
for var in [10,20,30,40,50]:
    r = f1(var)
    L.append(r)
print(L)
#
print("\n\n") 
# 
print([var+100 for var in [10,20,30,40,50]])

'''
1. lambda 
2. list comprehension
3. iterator
4. generator
|
5. map,filter 
---------------------------------
'''
