#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

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
h = max(A, B, C)
s = min (A, B, C)
m = (A + B + C) - (h + s)
#   x**2 + y**2 = h**2
p = (s**2) + (m**2)
k = math.sqrt(p)
j = h * 1.02
o = j - h
if k > o:
    print("that is a right triangle")
elif k < o:
    print("that is an acute triangle")
elif k == o:
    print("that is an obtuse triangle")
