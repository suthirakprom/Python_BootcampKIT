def oct_to_hex(num): 
    try: 
        test = int(num) + 1
        num1 = str(num)
        res = int(num1, 8)
        hexa = hex(res).upper()
        total = hexa.replace("0X", '')
        print(total)
    except:
        print("This is not an octal number")


oct_to_hex(1271)