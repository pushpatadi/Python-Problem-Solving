username = input("Enter Username: ")
if username == "Pushpa":
    password = int(input("Enter password: "))
    if password == 1234:
        OTP = int(input("Enter OTP: "))
        if OTP == 5678:
            print("Login Successful")

        else:
            print("Invalid OTP")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")
    