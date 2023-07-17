#normal method
class operator:
    def __init__(self,a):
        self.a=a
        print(self.a+self.a)
obj1=operator(15)
obj2=operator(25)
print('sum:',obj1.a+obj2.a)

#using operator overloading:
class oper:
    def __init__(self,a):
        self.a=a
    def __add__(Self,b):
        return Self.a+b.a
    
a=oper(55)
b=oper(44)
print(a+b)