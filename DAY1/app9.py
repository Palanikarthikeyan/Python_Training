# Arithmetic Operation - Calculation (input and output) int/float
# -----------------------------------------------------------------
# String Operation   + * 
print('Hello'+'python'+str(3.14)+'version') 
print('-'*15)
# Relational operators < > <= >= == !=
# ---------------------
# inputs are int,float,str -> bool (True/False)
#           ==============
print(150>100)
print(150 <100)
print(98.45 > 0.34)
print("root" == "root")
print("root" == "Root")
# Logical operators and or not
# ---------------------
# inputs are int,float,str -> bool (True/False)
#           ==============
# Single conditional statement test more than one condition
print(150>100 and 98.45 > 0.34)
print(150>100 or 98.45 < 0.34)
print(not (True))

# membership operators in not in
# in 
# not in
# -------
# inputs are collection  -> bool(True/False) 
#            |->str bytes list tuple dict set
#
# input_string_pattern in inputCollection -> True/False
# ====================    =============== 
print('s' in '101,raj,sales,pune') # True
print('x' in '101,raj,sales,pune') # False
print('e' in '101,raj,sales,pune') # True
print('sl' in '101,raj,sales,pune') # False
    #  ==              | |
print('sa' in '101,raj,sales,pune') # True 
print('sa' not in '101,raj,sales,pune') # False
# --------------------------------------------------
# identity operators is is not
# is 
# is not
# 10 20 -1 -2 0 34 253534352353534354343 //int - class
# -- --
# 10.0 0.0 ... //float - class
#
print(isinstance(10,int))
print(isinstance(10,str))

print(type(10) is int)
print(type(10) is str)