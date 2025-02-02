a=int(input("Enter a number: \n"))
print("You entered: ", a)

if (a%2)==0 and a!=0:
    print("The number entered is even")
elif (a%2)!=0:
    print("The number entered is odd")
elif(a==0):
    print("The numbmer is zero")