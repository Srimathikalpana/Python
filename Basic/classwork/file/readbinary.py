from pickle import *
name=open("srimathibiodat.doc","rb")
'''
while True:
    try:
        studentdata=load(name)
        print(studentdata)
    except EOFError as e:
        break'''
#if need to be taken alone
content=load(name)
print(content)
content1=load(name)
print(content1)
content2=load(name)
print(content2)
name.close()