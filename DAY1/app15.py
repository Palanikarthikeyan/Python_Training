
var = input('Enter your name:')
if(var.isupper()):
    print(f"Hello...{var}")
    print(f"Total no.of chars:{len(var)}")
else:
    var = var.upper()
    print(f"Hello {var}")

s1 = '45'
s2 = 'abc'
# int(s1) + 100 # OK
# int(s2) + 100 # Error

if(s1.isdigit()):
    print(f"updated value:{int(s1)+100}")
else:
    print(f'sorry the given string {s1} is not numerical chars')

if(s2.isdigit()):
    print(f"updated value:{int(s2)+100}")
else:
    print(f'sorry the given string {s2} is not numerical chars')

# ----------------------
# count()
#---------------

# how to use string count method in conditional statement
text = 'banana'
if text.count('a') == 0:
    print(f"There is no char 'a' found in the given string {text}")
else:
    print(f"the char 'a' is found  {text.count('a')} occurrence")
# 
text = 'banana'
if text.count('Y') == 0:
    print(f"There is no char 'Y' found in the given string {text}")
else:
    print(f"the char 'Y' is found  {text.count('Y')} occurrence")
# 