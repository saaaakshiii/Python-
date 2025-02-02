import math

def reverse(number):
    ans=0
    x=number
    while(x):
        ans=(ans*10)+(x%10)
        x=math.floor(x/10)
    
    return ans

for i in range(500, 1001):
    if(i==reverse(i)):
        print(i)