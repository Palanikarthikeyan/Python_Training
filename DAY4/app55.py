L = []
def f1(a):
    return a + 100

for var in [10,20,30,40,50]:
    r = f1(var)
    L.append(r)

print(L)
print("\n")
## -----------------------------------------------
# map() -> map(function,collection) -> generator
#          -------------------------

print(list(map(lambda a: a+100,[10,20,30,40,50])))

d={}
d['K1'] = list(map(lambda a: a+100,[10,20,30,40,50])) 

for var in list(map(lambda a: a+100,[10,20,30,40,50])):
    print(var)

# filter() -> filter(function,collection) ->generator
# ---------
#    |->filter True value Only 
'''
>>>
>>> def f1(a):
...     return a > 100
...
>>> for var in [150,50,200,30,400]:
...     r = f1(var)
...     print(r)
...
True
False
True
False
True
>>> list(map(lambda a: a>100,[150,50,200,30,400]))
[True, False, True, False, True]
>>>
>>>
>>> list(filter(lambda a: a>100,[150,50,200,30,400]))
[150, 200, 400]
>>>
>>> list(map(lambda a: a+100,[150,50,200,30,400]))
[250, 150, 300, 130, 500]
>>>
'''
