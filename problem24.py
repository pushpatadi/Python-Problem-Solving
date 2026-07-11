english = int(input("Enter English marks: "))
if english >= 35:
    maths = int(input("Enter Maths marks: ")) 

    if maths >= 35:
        science = int(input("Enter science marks: "))
        
        if science >= 35:
            print("pass")
 
        else:
            print("Fail in Scince")
    else:
        print("Fail in maths")
else:
    print("Fail in English")
         
         


