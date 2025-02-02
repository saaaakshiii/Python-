a=int(input("Enter any natural number: \n"))
print("You entered: ", a)

sum=0
for i in range(1, a+1):
    sum+=i

print("The sum upto ", a, " is: ", sum)