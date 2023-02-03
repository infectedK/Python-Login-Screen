from re import S

print("*** ESM Login screen ***");

userName ="Serkan"
password ="1234"

userName = input("Please enter user name")
Password = int(input("Please enter password"))

if (userName==userName) and (password != Password):
    print("User name true but password false")
elif(userName != userName) and (password == Password):
    print("Password true but user name false")
elif(userName !=userName) and (password != Password):
    print("USER NAME AND PASSWORD FALSE!!!")
elif(userName == userName) and(password == Password):
    print("Login Successful")    