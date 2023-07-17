class con:
    def __init__(self,place,mail,company):
        self.p=place
        self.m=mail
        self.c=company
    def func(self):
        print('place:',self.p)
        print('mail:',self.m)
        print('company:',self.c)
c=con('salem','kkalpana','tcs')
c.func()

class cons:
    def __init__(self,home,name):
        print('name:',name)
        print('home:',home)
a=cons('sj towers','sri')