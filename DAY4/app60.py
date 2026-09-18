import time
class vendor:
    '''Tranding application'''
    vName = ''
    vID = ''
    vGST = ''
    def initialization(self,vn,vid,vgst):
        self.vName = vn
        self.vID = vid
        self.vGST = vgst
        print(f'Vendor {self.vName} enrollment is done')
    def billing(self,pN,pQ=0,pcost=0.0):
        self.pname = pN
        self.pQ = pQ
        self.pcost = pcost
        self.total = self.pQ * self.pcost
        self.Tax = self.total * 0.18
        self.GS = self.Tax + self.total
        with open('billingInfo.log','a') as wobj:
            wobj.write(f'Vendor Name:{self.vName}\t GST:{self.vGST}\t Product:{self.pname}')
            wobj.write(f'Cost:{self.pcost}\t{self.Tax}\t{self.GS}\t')
            wobj.write(f'PO date/time:{time.ctime()}\n')

         
obj1 = vendor()
obj1.initialization('Klabs','V-101','VGSTBE123A')
obj1.billing('pA',5,1250.32)

time.sleep(5)

obj2 = vendor()
obj2.initialization('CTPL','V-102','VGSTBFA32A')
obj2.billing('pB',15,450.32)

obj3 = vendor()
obj3.billing('pC',12,1000)