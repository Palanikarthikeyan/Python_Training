fobj = open('C:\\Users\\karth\\emp.csv','r')
L=fobj.readlines()
fobj.close()
print(L)

wobj = open('C:\\Users\\karth\\r2.log','w')

wobj.write('data1\n')
wobj.write('data2\n')

wobj.close()
