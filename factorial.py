def factorial(n):
    if(n==0 or n==1):
        return n
    return n*factorial(n-1)

n=int(input("Enter any number: \n"))
print("You entered: ", n)

print("The factorial of ", n, " is: ", factorial(n))