'''
1. lambda 
===========
|-> python keyword
|-> Unnamed function 
|-> function call with arguments and return some value //
|-> lambda <list of args>:<basicOperation>
'''
def f1(a1,a2):
    return a1+a2

print(f1(10,20)) # named function call with args

print("\n") # empty line

f2 = lambda a1,a2:a1+a2
print(f2(10,20)) # unnamed function call with args

##################################
def f3(a1):
    return a1.upper()

print(f3('hello'))
##################################

f4 = lambda a1:a1.upper()
print(f4('hello'))
#################################
f5 = lambda a1:a1 >100
print(f5(150))

def fx(arg):
    if(arg >100 and arg<200):
        return arg + 150
    elif(arg> 300 and arg<500):
        return arg + 500
    else:
        return arg + 1000
#######
# fx(120)
# fx(350)
# fx(600)
########
f6 = lambda a : fx(a)
print(f6(120))
print(f6(350))
print(f6(600))

##
employees = [{"name":"arun","salary":50000},
             {"name":"balu","salary":35000},
             {"name":"chan","salary":70000}]

employees.sort(key=lambda emp:emp['salary'])
for var in employees:
    print(var)