# set - Collection of unordered items - unique items
# ----
#  |--> NOT index based access
#  |--> NOT Key:Value based access
#  |--> We can add new data ; we can delete an existing data
#  |--> There is no modification 
#  |--> unique items - there is no duplicate items

s = {10,20,30,10,20,10,20,20,10,20,30}
print(type(s))
print(len(s))
print(s)

s.add(40)
s.add('data')
s.add(20)
s.update([10,45,'data1','data2','data3']) 
print(s)
# ----
s.remove(20)
s.discard(30) 
print(s)

file1 = ['data1','data2','data3','data4','data5']
file2 = ['data5','data6','data3','data7','data2']

# union
uniq_data = set(file1) | set(file2) # <or> set(file1).union(set(file2))
print(uniq_data)

# intersection
common_data = set(file1) & set(file2)  # <or> set(file1).intersection(set(file2))
print(common_data)

# difference
only_in_file1 = set(file1) - set(file2)  # <or> set(file1).difference(set(file2))
print(only_in_file1)


# difference
only_in_file2 = set(file2) - set(file1)  # <or> set(file2).difference(set(file1))
print(only_in_file2)

# symmetric difference
exclusive_data = set(file1) ^ set(file2)  # <or> set(file1).symmetric_difference(set(file2))
print(exclusive_data)

