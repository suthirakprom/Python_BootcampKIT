def dec_to_oct(num):
    arrOct = [0] * 20 
    n = 0
    while(num!=0):
        arrOct[n] = num % 8
        num = num // 8
        n += 1

    for i in range(n-1, -1, -1):
        print(arrOct[i], end='')

dec_to_oct(98)