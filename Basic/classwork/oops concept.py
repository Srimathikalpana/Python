 #basic's of oops
class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def hi(self):
        print(self.n,self.c)
c=college('psg','cse')
c.hi()


