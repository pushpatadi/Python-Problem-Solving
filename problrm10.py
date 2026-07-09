a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before  swap")
print("First Number:", a)
print("Second Number:", b)

temp = a
a = b
b = a - temp


print ("Ater Swap")
print("first Number:", a)
print("Second Number:", b)