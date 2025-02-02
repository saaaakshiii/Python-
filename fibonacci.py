def fibo(n):
    if n==1 or n==0:
        return n
    return fibo(n-1)+fibo(n-2)

n=int(input("Enter any number: \n"))
print("You entered: ", n)
print("Fibonacci number upto ", n, " is: ", fibo(n))
