import math

def reverse(number):
    ans=0
    x=number
    while(x):
        ans=(ans*10)+(x%10)
        x=x//10
    
    return ans

a=int(input("Enter any number:\n"))
print("Number entered: ", a)

print("The reverse of ", a," is: ", reverse(a))

if(a==reverse(a)):
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")