#!/usr/bin/python3.6
import re   #import regular expressions
import getpass

print (chr(27) + "[2J") #this will add empty lines (to clear the screen) prior to running the program, to improve the command line users experience.

print ("\n\nCreate a new password that is between 6-12 characters long. A strong password contains at least one lowercase and uppercase letter, at least one digit and at least one special character.")
def main():
    password=getpass.getpass("\n\nEnter password: ")
    x = True    # x is just a random variable set to True
    while x:    # as long as x is True, then run the below loop
        if (len(password)< 6):  #if password less then 6 characters long then exit loop
            print("\nYour password is too short")
            break
        elif (len(password)> 12): #if password is more than 12 characters long then exit loop
            print("\nYour password is too long")
            break
        elif not re.search("[a-z]",password): #if password doesn't have one lowercase letter then exit loop
            print("\nYour password should contain at least one lowercase letter")
            break
        elif not re.search ("[A-Z]",password): #if password doesn't have at least one uppercase letter then exit loop
            print("\nYour password should contain at least one uppercase letter")
            break
        elif not re.search ("[0-9]",password):  #if password doen't have at least one digit then exit loop
            print("\nYour password should contain at least one digit")
            break
        elif not re.search ("[$#@&!*%?]",password):  #if password doen't have a special character then exit loop
            print("\nYour password should contain at least one special character (i.e. $#@&!*%?)")
            break
        elif re.search("\s",password):  #if password has any white space
            print("\nYour password shouldn't contain any white spaces")
            break
        else:
            print("Your password has been set!")
            x=False  #valid password has been created. Set x to False and exit loop
            break
    if x: #this is outside while loop
        print (" ")  #this print will be executed at each invalid input alongside the above individual messages that will be printed on exiting the loop
        main()
main()
