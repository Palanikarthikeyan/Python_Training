# Inheritance 

class A:
    pid = 101
    pname = 'pA'
    
class B:
    pcost = 1000
    
obj = B()
obj.pcost  # 1000
#obj.pid # AttributeError
#obj.pname # AttributeError

# class ChildclassName(ParentClassName)  
#        ------------  =============== //Inheritance 

class B(A): ###
    pcost = 1000

obj = B()
print(obj.pcost)
print(obj.pid,obj.pname)
