age = int(input('Input your age: '))
if age > 0 and age < 18: 
    print("You aren't adult yet... Sorry can't vote")
elif age >= 18: 
    print("You are eligible to vote")
else: 
    print("Age must be a positive digit")