# Name : Kimberley Gitau
# Date : 16/02/2026
# Program to calculate factorials of numbers


number = int(input("Enter the number x :"))
factorial = 1 #initialize factorial as 1
for x in range(1,number + 1):
    factorial *= x

print(f"{number}! = {factorial}")