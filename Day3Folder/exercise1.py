'''
Write a program to ask the user to enter a password.

If the password is correct, say "Access Granted"

Else, say "Access Denied"

The user is given a change to enter the password 3 times until the correct password is given.
If the user fails the 3rd attempt, the program will say "System Locked. I call police."

'''
answer = input("what is the hidden password?")
if answer == "passme":
    print("access is granted!")
else:
    print("wrong passowrd")