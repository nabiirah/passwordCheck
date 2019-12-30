#!/usr/bin/python3.6
##
import re   #import regular expressions

password=input("Enter password: ")
x = True    #x is just a random variable
while x:    #as long as x is True, then run the below loop
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search ("[A-Z]",password):
        break
    elif not re.search ("[0-9]",password):
        break
    elif not re.search ("[$#@]",password):
        break
    elif re.search("\s",password):  #if password contains white space  
        break
    else:
        print("Your password has been set!")
        x = False
        break   #exit the while loop

if x:
    print("Invalid Password")   #will exit program after printing this
