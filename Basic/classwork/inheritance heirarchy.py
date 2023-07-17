class college:
    def name(self):
        print('college is good')

class clgname(college):
    def name1(self):
        print('KSR college')

class clglocation(college):
    def name2(self):
        print('thiruchengode')

class placement(clgname,clglocation,college):
    def name3(self):
        print('good')

p=placement()
p.name()
p.name1()
p.name2()
p.name3()