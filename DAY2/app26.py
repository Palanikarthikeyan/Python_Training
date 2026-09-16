# List of List   --> [ [ ], [ ], [ ], [ ], []] 

# List of tuple    -> [(),(),(),(),()] 
# Tuple of List
# Tuple of tuple
# --------------------//nested 
L1 = [['Dx','Dy','Dz']] # List of list
L2 = [ ('D1,D2,D3'),('T1,T2,T3')] # Tuple inside the list
     # -----0th    |  --- 1st  
print(L1)
print(L1[0])
print(L1[0][0])

print(L2)
print(L2[1][0])
