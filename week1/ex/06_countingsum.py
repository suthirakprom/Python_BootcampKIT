num = ''
sum = 0
while num != 'stop':
    num = input("Input a number: ")
    if num == 'stop': 
        break
    try:  
        sum = sum + int(num) 
    except: 
        print("The input must an invalid number!")
print(f"Sum = {sum}")
 
