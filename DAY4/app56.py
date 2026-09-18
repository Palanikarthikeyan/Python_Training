'''
Exception Handling
---------------------
Error
=======
 |-> 1. Syntax Error - not following python rules 
 |-> 2. Logical Error - following python rules - logical mistakes 
 #      -------------
 #        Exception ----->Exit 
 #
 try :
     initialization/monitoring
 except <ExceptionName> as eobj:
     Handling the exception
 else: 
     There is No Error
 finally:
      Always running block
 ------------//keywords

Exception - pre-defined className
=========
'''
print("Test-1")
print("Test-2")
print("Test-3")
try:
    print(TEST)
except Exception as eobj:
    print("Error is occurred:",eobj)
else:
    print("No - Error")
finally:
    print("Done")
    
for var in [1,2,3]:
    total = var + 100
else:
    print("total = ",total)
print("End of the line")
print("\n---\n")

try:
    fobj = open('InvalidFile','r')
    s = fobj.read()
    fobj.close()
except Exception as eobj:
    print("Error:",eobj)
else:
    print(s)

# raise keyword:
# - is used to raise an exception manually
# - can be used with built-in or custom exceptions
# - syntax: raise ExceptionName("message")
#
# Example 1: Built-in exception
print("\n--- Raise Keyword Demo ---")
try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Valid age:", age)
except ValueError as e:
    print("Error:", e)
finally:
    print("Age check completed")



