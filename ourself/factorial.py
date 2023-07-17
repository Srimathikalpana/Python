a=int(input('enter the value'))

factor=1

if a>0 :
    for i in range(1,a+1):
        factor=factor*i
    print('The factorial of',a,'is',factor)
    
else: 
    print('not possible to give a factor')