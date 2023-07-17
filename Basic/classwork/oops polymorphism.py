class CUCKOO:
    def sound(self):
        print('cuckoo')
class peacock(CUCKOO):
    def sound(self):
        print('agaval')
class cocktail(CUCKOO):
    def sound(self):
        print('hoo')
class sparrow(CUCKOO):
    def sound(self):
        print('kichu kich')

obj1=sparrow()
obj2=peacock()
obj3=cocktail()
obj4=CUCKOO()
obj1.sound()
obj2.sound()
obj3.sound()
obj4.sound()
