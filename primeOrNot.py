import math

def prime_or_not(number):
    
    if number<2:
        return False
    elif number==2 or number==3:
        return True
    elif number%2==0 or number%3==0:
        return False
    
    for i in range(5, math.sqrt(number)+1, 2):
        if number%i==0:
            return False
    
    return True

number=int(input("Enter any number: \n"))

if(prime_or_not(number)):
    print(number, " is prime")
else:
    print(number, " is not prime")