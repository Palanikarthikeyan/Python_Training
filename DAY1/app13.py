# string 
# -------
# |->Collection of chars
# |->Index based access
# |->string is immutable 
# |-> '' <or> "" 
# |-> multiline string '''  '''  """   """
# 
s = 'python' # | p | y | t | h | o | n |
#            # | 0 | 1 | 2 | 3 | 4 | 5 | <== index
#               -6  -5  -4   -3  -2  -1  <== index
#
print(s)
print(s[0])
print(s[1])
print(s[5])
#print(s[7]) # IndexError 
print(len(s))
s='python is a general purpose programming language'
print(len(s))
#print(s[0])
#print(s[1])

#Slicing
#-------- group of chars / range of chars
#
#string_name[n:m] <== from nth index to m-1 index
print(s[7:16]) # from 7th index to 15th index(16-1)

#string_name[n:] <== from nth index to ALL
print(s[7:])

# string_name[:m] <== from 0th index to m-1 index
#           -----
print(s[:7]) # 1st 7chars/ 0 to 6th

# More slicing examples
# ---------------------
print(s[0:10])      # characters from index 0 to 9
print(s[10:])       # characters from index 10 to end
print(s[:10])       # characters from start to index 9
print(s[::2])       # every 2nd character
print(s[1:20:3])    # start at 1, stop before 20, step 3
print(s[::-1])      # reverse the string
print(s[-5:-1])     # last 4 characters except the last one
print(s[-1:-6:-2])  # characters from end with step 2

# note: s[a:b:c] => start at a, stop before b, move by c 
