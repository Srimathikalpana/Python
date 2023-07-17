def hello():
    print('hello! I am sri')
hello()

def info(name,age):
    print(name,age)
info('srimathikalpana',17)

def sakthi():
    tamil=int(input("enter the mark"))
    english=int(input('enter the mark'))
    if tamil==english :
      print('tamil and english are equal')
    elif tamil<=english:
        print('scored more in english')

    else:
        print('fail in both subjects')
sakthi()

#for loop
def jersh():
    for i in range (0,10):
        print(i)
    for x in range (0,100,2):
        print(x)

jersh()