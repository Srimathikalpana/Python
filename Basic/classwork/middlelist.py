#insert
a=[1,2,3,4,5,6,7]
print("original list:",a)
value=int(input("enter the value:"))
position=int(input("enter the position:"))
a.insert(position,value)
print("new list:",a)