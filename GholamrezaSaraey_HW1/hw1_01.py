username = input("Insert username: ")
password = input("Insert password: ")

if username == "admin" and password == "admin":
    print ("Welcome")
elif username == "admin" and password != "admin":
    print ("Wrong Data")
else:
    print ("Hello", username)