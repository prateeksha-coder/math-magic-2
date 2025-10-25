numL=int(input("Enter larger number: "))
numS=int(input("Enter smaller number: "))
prod=numL*numS
while(numS):
    numStore=numS
    numS=numL%numS
    numL=numStore
lcm=prod//numL
print("HCF is: ",numL)
print("LCM is:  ",lcm)