'''This is about demo module for vendor trading'''
import time
class vendor:
    '''Tranding application'''
    def __init__(self,vn,vid,vgst):
        '''this vendor enrollment initialization method - constructor'''
        self.vName = vn
        self.vID = vid
        self.vGST = vgst
        print(f'Vendor {self.vName} enrollment is done')
    def billing(self,pN,pQ=0,pcost=0.0):
        '''this is non-constructor billing method'''
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
