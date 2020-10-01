#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
num = input("Enter a number")
nom = float(num)
if nom < 0:
    print("negative")

elif nom == 0:
    print("zero")


else:
    print("positive")
