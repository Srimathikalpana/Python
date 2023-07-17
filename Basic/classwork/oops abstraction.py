from abc import ABC        #syntax
class bus(ABC):           #ABC means abstract statement
    def volvo(self):
        print("haiii")
        pass     
          #jumping statement
class SRT(bus):
    def volvo(self):
        print('It is a luxury bus')
class KPN(bus):
    def volvo(self):
        print('AC BUS')
class SAT(bus):
    def volvo(self):
        print('luxury vehicle')
                                       
obj1=SRT()
obj1.volvo()
obj2=KPN()
obj2.volvo()
obj3=SAT()
obj3.volvo()
b= bus()
b.volvo()