# Name : Kimberley Gitau
# Date : 16/02/2026
# Program to calculate means of numbers

# Average of the firt ten numbers
sum = 0

for x in range (0,10):
    sum = sum + x
print(f"mean : {sum/10}")

# Average of the first 100 numbers
sum1 = 0

for x in range(0,100,2):
    sum1 = sum1 + x

print(f"mean of even numbers : { sum1/50}")

# shortcut for getting the mean
# % = modulus
print(3 % 2)
