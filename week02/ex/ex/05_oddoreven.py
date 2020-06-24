num = input("Input a number:\n")

try: 
    cal = int(num) % 2
    if cal == 1: 
        print("Odd Number")
    else: 
        print("Even Number")
except: 
    print("Not a valid Number") 
