# Name : Kimberley Gitau
# Date : 16/02/2026
# Program to tabulate trigonometric ratios

import math
print("_________________________________________________________________________")
print(f"|  x   |   sin x        | cos x           |    tan x           |")
for x in range(-180,210,30):
    print(f"|   {x}    |   {math.sin(-180)} |   {math.cos(x)} |  {math.tan(x)} ")

for x in range(-180,180,30):
        print(f"|   {x}  |  {math.sin(-180)} |  {math.cos(x)} | {math.tan(x)} ")

for x in range(-180,180,30):
    print(f"|   {x} |   {math.sin(-180)} |  {math.cos(180)} |  {math.tan(30)} |")