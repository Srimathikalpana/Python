#class and object with class & instanse attribute
class a:
    name="kutty"   #class attribute
    def __init__ (self,ss1):     #instance attribute
        self.ss1=ss1

obj1=a("kalapana")
obj2=a("sri")


print("he is {}".format(obj1.__class__.name))
print("This is k{}".format(obj2.__class__.name))
print("car is {}".format(obj1.ss1))
print('my name is {}'.format(obj2.ss1))

#class and object method
class car: 
    def __init__(self,name):
        self.name = name
    def luxury(self):
        print('its a costly car for {}'.format(self.name))
c=car('BMW')
c1=car('Audi')
c.luxury()
c1.luxury()