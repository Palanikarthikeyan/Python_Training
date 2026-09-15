# print()
# type()
# dir()
# ...
# functionCall()
# Vs
# object.function() <-- methodcall
#        ---------  
s="python"
print(s.upper()) # methodCall 
print(s.title()) 
print("s=",s)
s = s.upper()
print(s)
s='data\n'
print(s.strip()) # remove \n chars \t space 
print("welcome to python".title())

# strip() removes leading and trailing whitespace (or specified characters) from a string.
print("  hello  ".strip())
print("---python---".strip("-"))

# prompt -> upper() strip()     lower()
# ------   -----------  ------  --------
# Two different examples using upper():
print("hello world".upper())
name = "karth"
print(name.upper())
#

 