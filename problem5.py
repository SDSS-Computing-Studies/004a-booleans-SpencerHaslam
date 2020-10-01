#! python3

#  In math, if a quadratic equation is in the format
# ax^2 + bx + c = 0, the discriminant can be calculated as
# b^2 - 4 * a * c
# If the discriminant is a perfect square, the equation can
# be factored.  Furthermore, if the discriminant is negative,
# then the equation has no solutions (not used in this assignment).
# Have the user enter in values for a, b and c and then 
# tell them if the equation can be factored.

# Inputs:
# - 3 numbers (a, b, c)

# Outputs:
# - "the equation can be factored"
# - "the equation can not be factored"
import math
a = input("Enter a number")
b = input("Enter a second number")
c = input("Enter a third number")
A = float(a)
B = float(b)
C = float(c)
sol = B**2 - 4 * A * C
try:
    sq = math.sqrt(sol)
    print(sq)
except:
    print("You can't square root a negative")
    exit()

fsq = float(sq)
print(fsq)
print(sol)
# sol = discriminant
# fsq = sqrt(discrinant) as calculated in line 27
i = int(fsq)
f = float(fsq)

if f == i:
    print("the equation can be factored")

else:
    print("the equation can not be factored")
