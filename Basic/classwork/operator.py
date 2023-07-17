#arithmetic
a=50
b=25
print("addition:",a+b)
print("subraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("modulo:",a%b)

#logical
a=True
b=False
print("and operator:",a and b)
print(" or operator:", a or b)
print("not operator:",not a)
#what if condition is given
s=30
print(s>a and s<b)     #here a and b are taken from arithmetic variable
print(s<a or s>b)

#assignment
a=20
b=a
print(b)
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)

#comparison
a=15
b=22
print("greater than:",a>b)
print("less than:",a<b)
print(a<=b)
print(a>=b)
print(a==b)