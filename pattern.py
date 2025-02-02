n=int(input("Enter any number:\n"))
print("You entered: ", n)

# for i in range(1, n + 1):  # Loop from 1 to 5
#     print("*" * i)

for i in range(n, 0, -1):
    print("*"*i) #print i number of stars in each row