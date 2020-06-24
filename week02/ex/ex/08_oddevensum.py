num = input("Input a number: ")
evenSum = 0
oddSum = 0
try:
    num2 = int(num)/2
    for i in range(1, int(num)+1): 
        if i % 2 == 0: 
            evenSum = evenSum + i
        else: 
            oddSum = oddSum + i
    print(f"Sum of odd numbers = {oddSum//num2}")
    print(f"Sum of even numbers = {evenSum//num2}")
except:
    print("Invalid Input")
    print(f"Sum of odd numbers = {oddSum}")
    print(f"Sum of even numbers = {evenSum}")