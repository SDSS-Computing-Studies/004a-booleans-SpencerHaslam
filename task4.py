#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"


#Strings
#*needle* in *haystack*
#"i" in "team" is evaluated as False
#"fun" in "funeral" is evaluated as True

#if "fun" in "funeral":
#    print("there is fun in funeral")

#if 3 in range(1,10):


num = input("Enter a sentence")
if "password" in num:
    print("the sentence contains password")


else:
    print("the sentence does not contain password")
