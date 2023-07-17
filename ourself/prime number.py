a=int(input('enter the value'))
for i in range(2,a+1):
    for n in range (2,i):
        if i%n ==0:
            break
    else:
        print(i)
