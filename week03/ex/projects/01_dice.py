import random

welcome_message = "Welcome to the dices game!"
warning_message = "USAGE: The number must be between 1 and 8"
flag = True
sum = 0
print(welcome_message)
while flag:
    try:
        n = int(input("Enter the number of dices you want to roll: "))
        if n<1 or n>8:
            n = 10/0
        else: 
            flag = False
    except: 
        print(warning_message)
        flag = True
if n>1:  
    for i in range(1,n+1):
        random_number = random.randint(1,6)
        sum += random_number
        print(f"Dice {i} : {random_number}")
    print("="*10)
    print(f"RESULT: {sum}")
    print("="*10)
else:
    print(f"RESULT: {random.randint(1,6)}")

    
