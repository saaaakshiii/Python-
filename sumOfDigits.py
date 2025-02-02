import math

def sum_of_digits(n):
    ans=0
    
    while n!=0:
        ans+=(n%10)
        n=math.floor(n/10)
    
    return ans

n=int(input("Enter any number:\n"))
print("You entered: ",n)

print("The sum of digits is: ", sum_of_digits(n))