class Enrollment:
    Name = ''
    DOB = ''

obj1 = Enrollment()
obj1.Name = "Arun"
obj1.DOB = "1st Jan"

obj2 = Enrollment()
obj2.Name = "Anu"
obj2.DOB = "2nd Feb"
print(f'Emp name is:{obj1.Name} DOB is:{obj1.DOB}')
print(f'Emp name is:{obj2.Name} DOB is:{obj2.DOB}')

Enrollment.bloodgroup = "" # classname - create new attribute

obj1.bloodgroup = "A+" # object based initialization
obj2.bloodgroup = "O+" # object based initialization

print(f'{obj1.Name} BloodGroup is:{obj1.bloodgroup}')
print(f'{obj2.Name} BloodGroup is:{obj2.bloodgroup}')