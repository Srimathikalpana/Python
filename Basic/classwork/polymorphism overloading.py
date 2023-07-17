'''class sri:
    def aa(self,a):
        print(a)
    def aa(self,a,b):
        print(a+b)
    def aa(self,a,b,c):
        print(a+b+c)
s=sri()
s.aa(10,20,30)            #code runs only if 3 variables are given since only the last funct runs

class over:
     def load(self,a=None,b=None,c=None):
         if a!=None and b!=None and c!=None:
             return a+b+c
         elif a!=None and b!=None:
             return a+b
         else:return a
o=over()

print('sum',o.load(10,25))
'''
class values:
    def nos(self,*args):        # *args means any number of parameters can be given
      sum=40
      for i in args:
          sum+=i
          print('add values',sum)
v=values()
v.nos(20,30)
v.nos(30,20,100)
v.nos(30,20,100,200)
v.nos(10,20,30,100,200)
