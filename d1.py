# def decToBin(num):
#     if num>1:
#         decToBin(num//2)
#     print(num%2, end='')

# def decToOctal(num):
#     if num>1:
#         decToOctal(num//8)
#     print(num%2, end='')
    
# decToBin(4)
# decToOctal(64)

# def factorial(num):
#     if num==0 or num==1:
#         return num
#     return num*factorial(num-1)

# print(factorial(5))

def fib(num):
    if num==0 or num==1:
        return num
    return fib(num-1)+fib(num-2)

print(fib(6))
