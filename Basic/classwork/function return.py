#function with return type
def demo():
    exp=int(input('enter ur experience: '))
    skill=input('ur skill: ')
    if exp>=4 and exp<8 and skill=='python' or skill=='java':
        return 'promoted as team lead'
    elif exp>=10 and exp<14 and skill=='c++' or skill=='java':
        return 'promoted as HR'
    return 'be as a member'

designation=demo()  #assign a value to print the output
print(designation)