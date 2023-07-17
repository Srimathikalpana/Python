#append method
a=('sri','mathi','kalpana','hari','vicky')
b=list(a)
b.append('vijay')
a=tuple(b)
print(a)

#adding tuple in tuple
a=('sri','mathi','kalpana','hari')
b=('vicky','vijay..')
a+=b
print(a)