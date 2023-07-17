from threading import *
from time import sleep
class react(Thread):
    def __init__(self,aa):
        super().__init__()
        self.name=aa 
        self.click=[11,22,33,44,55,66,77,88,99,100]
    def run(self):
        print('welcome',self.name)
        for x in self.click:
            print(x)
            sleep(1)

a=react('srimathi')
b=react('nevetha')
c=react('jershilin')

a.start()
a.join()
b.start()
b.join()
c.start()
