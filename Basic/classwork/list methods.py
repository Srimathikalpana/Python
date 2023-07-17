#copy
list=[1,2,3,2,3,5]
a=list.copy()
print('copy:',a)
#count
count=a.count(3)
print(count)

print(len(list))
#run time input using for loop
aa=input("enter the value")
list=aa.split(",")
print("list names")
for i in list:
    print(i)
    

#looping using append
n=int(input("enter the list"))
list1=[]
for i in range(n):
    listname=input("enter the value")   
    list1.append(listname)           #to add the other term into the list at last
print("list:",list1)

a=['sri','mathi','kalpana','pm']
a.remove('mathi')
print(a)
