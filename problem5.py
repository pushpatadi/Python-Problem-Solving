P = int(input("Enter principal amount:"))
R = int(input("Enter rate of interest:"))
T = int(input("Enter time in years:"))

SI = (P * R * T) / 100


print("----SIMPLE INTEREST----")
print("Principal:", P)
print("Rate:", R)
print("Time:", T)
print("Simple Interest:", SI)