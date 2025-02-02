# a=(input("Enter any number of your choice: "))

# for i in range(1, 6):
#     print(a, "x", i, "=", a*i)

# a = int(input("Enter any number of your choice: "))  # Convert input to integer
# print("You Entered: ", a)

# for i in range(1, 6):
#     print(a, "x", i, "=", a * i)  # Perform multiplication correctly

a=int(input("Enter a number upto which you want a table of 5\n", ))
print("You entered: ", a)

for i in range(1, a+1):
    print("5 x ", i, "= ", 5*i)
