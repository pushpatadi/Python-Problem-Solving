pin = int (input("Enter your PIN: "))

if pin == 1234:
    amount = int(input("Enter amount: "))
    if amount <= 5000:
        print("Transaction Successful")  
    else:
        print("Insufficient Balance")

else:
    print("Invalid PIN")

