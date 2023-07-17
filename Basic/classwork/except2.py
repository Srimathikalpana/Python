try:
    password=input("set the password")
    confirm=input("confirm the password")
    if password!=confirm:
        raise passworderror
    else:
        print('password was set successfully')
 
except passworderror as an:
    print(an)
finally:
    print("login successful!")