# List Comprehension - List Append Operation
# ==================

L = []
for var in [10,20,30,40,50]:
    r = var + 100
    L.append(r)
print(L)

# [finalValue for iterable]
#             -----(1)----
# ----(2)----

print([var+100 for var in [10,20,30,40,50]]) ## list comprehension 
### 
print ("\n#########") # empty line
L = []
for var in [10,20,30,40,50]:
    if(var > 30):
        r = var + 100
        L.append(r)
    else:
        r = var + 500
        L.append(r)

print(L)
print ("\n#########") # empty line
print([var+100 if var >30 else var+500 for var in [10,20,30,40,50]]) ## list comprehension
'''
>>> CSV_files = []
>>> for var in os.listdir("."):
...     if 'csv' in var:
...         CSV_files.append(var)
...
>>> len(CSV_files)
30
>>>
>>> CSV_files1 = [var for var in os.listdir(".") if 'csv' in var]
>>>
>>> len(CSV_files1)
30
>>>
'''
