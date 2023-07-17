class travels:
    def name(self):
        print('ok travels')
class travels1:
    def name1(self):
        print('kpn travels')
class main(travels,travels1):
    def name2(self):
        print('happy journey')

m=main()
m.name()
m.name1()
m.name2()

