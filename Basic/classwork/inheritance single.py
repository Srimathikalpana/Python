'''types of inheritance
*single
*multilevel
*multiple
*hierarchy
'''
#single
class bike:
    def gear(self):
        print('5km speed gear box')
class car(bike):
    def benz(self):
        print('is a costly car')
c=car()
c.benz()
c.gear()