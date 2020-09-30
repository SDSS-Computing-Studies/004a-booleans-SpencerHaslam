#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks
a = input("Enter a username")
A = str(a)
c = str("admin")
d = str("12345password")
if c == A:
    b = input("Enter a password")
    B = str(b)
    if d == B:
        print("Access granted")
    
    else:
        print("Incorrect password")

else:
    print(A + " is an invalid user")
