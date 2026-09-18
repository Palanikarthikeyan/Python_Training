
# iterator
# ----------
#  |-> object - allows user to access element one at a time
#  
#  iter() -> creates / gets an iterator
#  next() -> gets the next value from the iterator
#  ---------  
#     |->StopIteration 

s='hello'
for var in s:
    print(var)

# 
################## 
# Vs - internal  
it = iter("hello")

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
# 
################## 
# 
it = iter("hello")
for var in it:
    print(var)