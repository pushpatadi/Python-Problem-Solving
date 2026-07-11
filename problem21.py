age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("Do you have Voter ID? (yes/no): ")
    if voter_id == "yes" :
        print("Eligible to Vote")

    else:
        print("Not Eligible to Vote(No Voter ID)")

else:
    print("Not Eligible to Vote(Age is below 18)")
    