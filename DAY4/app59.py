class Enrollment:
    Name = ''
    DOB = ''
    def f1(self,name,dob):
        self.Name = name
        self.DOB = dob
        print(f'{self.Name} Enrollment is done!')
    def f2(self):
        print(f'About {self.Name} details:-')
        print(f'Emp name :{self.Name} DOB:{self.DOB}')

obj1 = Enrollment()
obj1.f1('Arun','1st Jan')

obj2 = Enrollment()
obj2.f1('Anu','2nd Feb')
obj1.f2()
obj2.f2()