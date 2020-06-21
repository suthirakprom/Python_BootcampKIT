def oct_to_dec(num): 

    try: 
        n = 0
        num1 = int(num)
        # base value
        base_value = 1

        while(num1!=0): 
            last = num1 % 10 
            num1 = num1 // 10 
            n += last * base_value
            base_value = base_value * 8
        
        print(n)

    except: 
        print("This is not octal number")

oct_to_dec(750)