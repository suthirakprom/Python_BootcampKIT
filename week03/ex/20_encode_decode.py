abc = "abcdefghijklmnopqrstuvwxyz"
string2 = ""
again = True
while again:
    choice = int(input("Press 1 to encode\nPress 2 to decode\n"))
    if choice == 1: 
        string = input("Enter a string to encode:\n")
        for i in string: 
            string2 += abc[(abc.find(i)+13)%26]
        print("The decoded text is:",string2)
        string2 = ""
    elif choice == 2: 
        string = input("Enter a string to decode:\n")
        for i in string: 
            string2 += abc[(abc.find(i)-13)%26]
        print("The encoded text is:",string2)
        string2 = ""
    pick = input("Do you want to continue? [Y/N]")
    if pick == 'N': 
        again = False
    elif pick == "Y": 
        again = True
    else:
        print("Invalid input\nExit the program")
        again = False
        
