# Name : Kimberley Gitau
# Date : 17/02/2026
# Program to display diamond using *

n = int(input("Enter number of rows (half): "))

# Upper part
for i in range(1, n+1):
    print(" " * (n-i) + " * " * i)

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n-i) + " * " * i)

# Program to display triangle using *

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    print(" * " * i)

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(f"\nQuadratic equation: {a}x^2 + {b}x + {c} = 0")

d = b**2 - 4*a*c  #discriminant

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots:")
    print("x1 =", x1)
    print("x2 =", x2)

elif d == 0:
    x = -b / (2*a)
    print("One real root:")
    print("x =", x)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex roots:")
    print("x1 =", real, "+", imag, "i")
    print("x2 =", real, "-", imag, "i")



