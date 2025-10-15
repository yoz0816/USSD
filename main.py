balance = 100  # Starting balance

while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Exit")
    
    option = input("Enter option: ")

    # -------------------------------
    # Group 1: Check Balance
    if option == "1":
        print("you balance is", balance,"birr")
        

    # -------------------------------
    # Group 2: Buy Data
    elif option == "2":
        print("1.100MB in 5 birr")
        print("2.250MB in 15 birr")
        print("3.500MB in 25 birr")
        choice=input("select this choices: ")
        if choice =="1":
            if balance>=5:
                balance-=5
                print("you have sucessfully purchase 100MB in 5 birr")
            else:
                print("you have insufficient balance to purchase this")
        elif choice=="2":
             if balance>=15:
                 balance-=15
                 print("you have sucessfully purchase 250MB in 15 birr") 
             else:
                 print("you have insufficient balance to purchase this")
        elif choice=="3":
            if balance>=25:
                 balance-=25
                 print("you have sucessfully purchase 500 MB in 25 birr")
            else :
                 print("you have insufficient balance to purchase this")
        else:
             print("invalid entry\nplease try again")
    # -------------------------------
    # Group 3: Buy Airtime
    elif option == "3":
        try:
            airtime=int(input("enter airtime amount: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if airtime<= balance:
                balance -=airtime
                print("you have sucessfully purchase", balance)
            else:
                print("insufficient balance")
    
    # -------------------------------
    # Group 4: Exit & Invalid Input
    elif option == "4":
        exit()

    else:
        print("invalid input")
