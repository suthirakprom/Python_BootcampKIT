def fun_calc(num1,num2,operator):
    if operator == '+':
        print(f"Product: {num1+num2}")
        print(f"Process: {num1} {operator} {num2} = {num1+num2}")
    elif operator == '-':
        print(f"Product: {num1-num2}")
        print(f"Process: {num1} {operator} {num2} = {num1-num2}")
    elif operator == '*':
        print(f"Product: {num1*num2}")
        print(f"Process: {num1} {operator} {num2} = {num1*num2}")
    elif operator == '/':
        print(f"Product: {num1/num2}")
        print(f"Process: {num1} {operator} {num2} = {num1/num2}")

fun_calc(50,2,"*")