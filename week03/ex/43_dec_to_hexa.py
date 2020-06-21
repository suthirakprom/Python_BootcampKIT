def dec_to_hexa(num):
    arrHex = [0] * 20
    n = 0
    while(num!=0):
        r = num % 16
        num = num //16
        if r < 10:
            arrHex[n] = r
            n += 1
        else: 
            arrHex[n] = chr(r+55)
            n += 1
        
    for i in range(n-1, -1, -1):
        print(arrHex[i], end='')

dec_to_hexa(1500)
        