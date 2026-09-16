# python supports multiple initialization
# variable = value
# -------------------
# variable1,variable2,variable3,...Vn = Value1,Value2,Value3,...Vn

prod_name = 'pA'
prod_id = 101
prod_cost = 1000
### Vs
prod_name,prod_id,prod_cost = 'pA',101,1000  # multiple initialization

# Va,Vb,Vc = 10,20,30,40 ValueError: too many values to unpack (expected 3, got 4)

# Va,Vb,Vc,Vd = 10,20,30 ValueError: not enough values to unpack (expected 4, got 3)
emp_details = ['Mr.ABC','sales','E101','Pune']
ename = emp_details[0]
edept = emp_details[1]
eid = emp_details[2]
ecity = emp_details[-1]
####### Vs 
EmpName,Edept,EID,ECity = emp_details

# input_string -> output_list
# input_string.split(sep) ->[]
#              ==========
s = "101,raj,sales,pune,1000" # len(s) -> total no.of chars count
#print(s.split(","))
L = s.split(",")
eid,ename,edept,ecity,ecost = s.split(",") # L
print(f'{eid}\t{ename.title()}\t{ecity.upper()}')

# Given string
s = "root:x:bin:bash:usr:admin"
print(type(s)) # 1. determine the give s value type
print(len(s)) # 2. count the no.of items from the given string(s)
L = s.split(":") # 3. based : split into multiple items 
print(type(L),len(L)) # 4. count the no.of items from output list

# input_string ->output_list - split()
# Vs
# input_list -> output_string - join()
# ------------
# Prompt -> join() and how to use join input list
#
L = ['101','raj','sales','pune','1000']

s = ",".join(L)
print(s,type(s))