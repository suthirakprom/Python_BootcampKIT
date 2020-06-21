def bin_to_dec(num):
    str_num = str(num)
    incorrect = len(str_num)
    for n in str_num: 
        if n == '0':
            incorrect -= 1
        elif n == '1':
            incorrect -= 1
    if incorrect != 0:
        print("This is not a binary number")
    else:
        i, j= 0, 0
        while(num!=0): 
            temp = num % 10 
            i = i + temp * pow(2, j)
            j += 1
            num = num // 10
        print(i)

bin_to_dec(1001)