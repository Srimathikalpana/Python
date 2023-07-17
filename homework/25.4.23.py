'''print("if else")
score=int(input("enter the value"))
if score>=236:
    print("KKR won the match")
else :
    print("CSK won the match")'''

print("elif")
cost=input("enter the amount")
if cost> "rs100" and cost >"rs200":
    print("payment ssuccessfull")
elif cost>= "rs200":
    print("payment unsuccessful")
elif cost<= "rs200":
    print("payment successful")
else: print("yet payment not done")