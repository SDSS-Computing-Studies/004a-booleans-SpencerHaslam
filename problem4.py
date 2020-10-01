# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
a = input("Enter a number")
b = input("Enter a second number")
c = input("Enter a third number")
A = float(a)
B = float(b)
C = float(c)
uHyp = max(A, B, C)
minVal = min (A, B, C)
midVal = (A + B + C) - (uHyp + minVal)
#   x**2 + y**2 = h**2
p = (minVal**2) + (midVal**2)
cHyp = math.sqrt(p)
upperLimit = cHyp * 1.02
lowerLimit = cHyp * 0.98
if uHyp > upperLimit:
    print("that is an obtuse triangle")
elif uHyp < lowerLimit:
    print("that is an acute triangle")
else:
    print("that is a right triangle")
