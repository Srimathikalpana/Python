list=['hi','hello','welcome','hi','bye']
a=list.copy()
print(a)

print(list.count('hi'))

b='go'
list.append(b)
print(list)

list.insert(2,b)
print(list)

list2=[100,200,250,300,400]
print(max(list2))
print(min(list2))
print(sum(list2))

print(list2.pop(2))

ss=[1,2,3,4,5]
ss.reverse()
print(ss)
ss.remove(2)
print(ss)

value=int(input('enter the value'))
list1=[]
for i in range(value):
    a=input('enter the value')
    list1.append(a)
    print('list:',list1)
    