#consists of 2 blocks:try and except
'''try:                          #this programe tends to infinity which means an error 
    a=10                       #but we get the output as the reason for the error
    b=0
    c=a/b
    print(c)

except Exception as e:
    print(e)
    print('how are you?')

try:
    d=100
    e=0
    f=d/e
    print(f)
except ZeroDivisionError as e:
    print(e)

try:             #value error
   number=int(input('enter the value'))
   print(number)
except ValueError as a:
   print('value error:',a)
   print('hi')
try:             #name error
   name='sri'
   print(value)
except NameError as f:
   print(f)
'''
try:                   #index error.
   list=[11,22,33,44,55]
   print(list[6])
except IndexError as e:
   print('indexerror:',e)
#key error
try:
   dictionary={'Name':'sri','subject':'python'}
   print(dictionary['age'])
except Exception as r:
   print('Key error:',r)

#attribute error
try:
   class a:

      pass
   A=a()
   a.hello()
except AttributeError as s:
   print('Attribute error:',s)
