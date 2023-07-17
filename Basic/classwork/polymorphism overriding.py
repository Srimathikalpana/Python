class sri:
    def name(self):
        print('kutty')
class raja(sri):
    def name(self):
        super().name()
        print('kutty1')
class neve(raja):
    def name(self):
        super().name()
        print('mathi')
n=neve()
n.name()
