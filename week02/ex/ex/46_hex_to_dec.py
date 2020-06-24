def hex_to_dec(num):
    n = 1
    res = 0
    count = 0

    for i in range(len(num)):
        if num[i] > 'F':
            count += 1

    if count == 0:
        for i in range(len(num)-1, -1, -1):
            if num[i] >= '0' and num[i] <='9': 
                res += (ord(num[i])-48) * n
            elif num[i] >= 'A' and num[i] <= 'F': 
                res += (ord(num[i]) - 55) * n
                
            n = n * 16
        
        print(res)
    else: 
        print("This is not a hexa-decimal number")

hex_to_dec("BA1")

