#writes aprogram that asks the user for a password(as a string). if the password is "Secret123", print "Access granted", otherwise print "Access denied"
password = input("Enter your password: ")
if password == "Secret123":
    print(len(password))
    print("Access granted")
    #add controls to validate if it is a digit based password or string/character based password
    if password.isdigit():
        print("Password is numeric")
    elif password.isalpha():
        print("Password is alphabetic")
    else:
        print("Password contains a mix of characters and digits")
    
else:
    print(len(password))
    print("Access denied")
    #add controls to validate if it is a digit based password or string/character based password
    if password.isdigit():
        print("Password is numeric")
    elif password.isalpha():
        print("Password is alphabetic")
    else:
        print("Password contains a mix of characters and digits")
    