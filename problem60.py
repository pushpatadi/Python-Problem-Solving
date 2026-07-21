secret_number = 7
user_number = int(input("Enter your guess: "))
while secret_number != user_number:
    print("Wrong Guess! Try Again")
    user_number = int(input("Enter your new Guess: "))
print("Congrats You guessed it !")
