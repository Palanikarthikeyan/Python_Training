T = ([],[],[]) # tuple of list
print(type(T))
print(type(T[0])) # list
T[0].append('D1')
T[0].append('D2')
print(T)

# Create a list of tuple records, initializing each record separately.
record1 = ('D1', 'Data 1',1000)
record2 = ('D2', 'Data 2',2000)
record3 = ('D3', 'Data 3',3000)
records = [record1, record2, record3,('D4','Data',4000)]

print(records)
print('Total number of records:', len(records))