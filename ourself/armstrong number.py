num = int(input('enter the value'))
order = len(str(num))

sum = 0

temp = num
print(temp)
while temp > 0:
   digit = temp % 10
   print(digit)
   qube=digit ** order
   print(qube)
   sum += qube
   print(sum)
   temp //= 10
   print(temp)

if num == sum:
   print(num,"is an Armstrong number")
else: 
   print(num,"is not an Armstrong number")