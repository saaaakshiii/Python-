def is_armstrong(n):
    num_digits = len(str(n))  # Calculate number of digits dynamically
    ans = 0
    x = n

    while x:
        digit = x % 10  # Extract last digit
        ans += digit ** num_digits  # Raise to the power of total digits
        x //= 10  # Remove last digit

    return ans  # Return the computed sum


n=int(input("Enter any number:\n"))
print("You Entered: ", n)

if(n==is_armstrong(n)):
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")