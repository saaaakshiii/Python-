# def sum_positive():
#     sum=0
    
#     while True:
#         num=float(input("Enter positive numbers (or a negative number to stop)"))
        
#         if(num<0):
#             break
#         else:
#             sum+=num
    
#     return sum

# print("The sum of numbers is: ", sum_positive())

#List comprehension

def list_comp(start, end):
    square_num=[num**2 for num in range(start, end+1) if num%2==0]
    return square_num

start=int(input("Enter start"))
end=int(input("Enter end"))

ans=list_comp(start, end)
print(ans, end=" ")
# for x in ans:
#     print(x, end=" ")

#celcius to fahrenheit using map function

# def celsius_to_f(celcius):
#     return (celcius*(9/5))+32

# celcius_temps=[0,10,20,30,40]
# fahrenheit=list(map(celsius_to_f, celcius_temps))

# print("Temperature from celcius to fahrenheit is: ", fahrenheit)

#using lambda function

# celcius_temps=[0, 10, 20, 30, 40]
# fahrenheit=list(map(lambda c: (c*(9/5)+32), celcius_temps))

# print("The temperature in fahrenheit is: ", fahrenheit)

# # Lambda function to filter out all the even numbers from a list

# num=[1, 2, 3,4, 5,6,7,8,9]
# ans=list(map(lambda x : x if x%2==0 , num))