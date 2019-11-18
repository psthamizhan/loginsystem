#input from user

Name=raw_input("Enter Your Name:")
user=raw_input("Enter User_Name:")
pas=raw_input("Enter password:")

#login process

if user=='admin':
    if pas=='ADMIN':
        print "Hai "+Name
    else:
        print "Wrong Password "
else:
    print "Wrong User"
