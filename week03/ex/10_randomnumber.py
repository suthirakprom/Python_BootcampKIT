import random
num = int(input("Input Number:"))
sumOfEven = 0
for i in range(num): 
    n = random.randint(2000,3000)
    if n % 2 == 0: 
        sumOfEven += n
print("Sum of even random numbers:", sumOfEven)