

from threading import *

class fiesta(Thread):
    def __init__(self,hi):
        super().__init__()
        self.name=hi
    def run(self):
        print("welcome",self.name)

f1=fiesta("srimathi")
f2=fiesta('nevetha')
f3=fiesta('jershlin')

f1.start()
f2.start()
f3.start()
