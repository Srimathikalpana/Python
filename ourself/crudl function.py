class books:
    def __init__(self,name,price,edition):

        self.n=name
        self.p=price
        self.e=edition
    def bookdetails(self):
        print('bookname:',self.n)
        print('price:',self.p)
        print('edition:',self.e)
    def __str__(self):
        return self.n+" "+str(self.p)+" "+str(self.e)+"\n"
# b=books('ponniyin selvan','rs.1000',2022)
# #b.bookdetails()
# #print(b)
# book2=books('the priest','rs 250',2006)
# #book2.bookdetails()
# #print(book2)
# book3=books('money heist','rs 500',2015)
# #book3.bookdetails()
# list=[b,book2,book3]
#for x in list:print(x)
# list[2].e=2022
# for x in list:print(x)

from pickle import *

# bookdata=open('file.doc','wb')
# dump(list,bookdata)
# print("data has written i the file")

bookdata=open('file.doc','rb')
myBooks=load(bookdata)
bookdata.close()
for x in myBooks:print(x)

# bookdata=open('file.doc','wb')
# myBooks[1].e=2023
# dump(myBooks,bookdata)
# print("Data has changed")
