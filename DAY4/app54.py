# Generator - type 
# -------------------
# function return an iterator (object) - generator
#          ---------------------------
#                 |-> yield <== pyth.,on keyword

# function - returns a generator 
#            -------------------
#                     |-> 1. next(generator_obj) ->value... StopIteration 
#                                     <or>
#                     |-> 2.  for var in generator_obj:
#                                          ...
#                                      <or>
#                     |-> 3. typecast to list => list(generator_obj) 

# return Vs yield 

def f1():
    return 10
    print("This line won't execute")


def f2():
    yield 10
    print("This line will execute")
    yield 20
    yield "D1","D2"
    
print(type(f1),type(f2))
print(type(f1()),type(f2()))

gen_obj = f2()
for var in gen_obj:
    print(var)
    
gen_obj = f2()
print(list(gen_obj))# typecast to list


### os.listdir('.') ->list 
# Vs
### os.walk('.') -> generator