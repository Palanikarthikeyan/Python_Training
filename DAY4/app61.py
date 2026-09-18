import time
class vendor:
    '''Tranding application'''
    def __init__(self,vn,vid,vgst):
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


obj1 = vendor('Klabs','V-101','VGSTBE123A')
obj1.billing('pA',5,1250.32)

time.sleep(5)

obj2 = vendor('CTPL','V-102','VGSTBFA32A')
obj2.billing('pB',15,450.32)

'''
obj3 = vendor() # Error
obj3.billing('pE',12,1000)
'''
obj3 = vendor('CosTools','V-313','VGST334SD2')
obj3.billing('pD',3,9393.31)
obj3.billing('pA',2,450.32)
