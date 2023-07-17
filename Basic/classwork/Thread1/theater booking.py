from threading import *

class booking(Thread):
    def __init__(self,aa):
        super().__init__()
        self.name=aa
        self.__total=50         #double underscore acces the variable privately within class
    
    def run(self):
        print('welcome',self.name,'to INOX multiplex')
        required=int(input('how many tikets are required?'))
        if required<=self.__total:
            print(required,'tickets has to issued',self.name)
        else:
            print('available is',self.__total)
a=booking('srimathikalpana')
b=booking('kalpana')
c=booking('hari')
a.start()
a.join()
b.start()
b.join()
c.start()