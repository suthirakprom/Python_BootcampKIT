def binary_substraction(num1, num2):
    sub_dec = num1 - num2
    bin1 = ''
    bin2 = ''
    if num1==0:
        bin1='0'+bin1
    else:
        while(num1 >0):
            bin1=str(num1%2)+bin1
            num1=num1//2
    
    if num2==0:
        bin2='0'+bin2
    else:
        while(num2 >0):
            bin2=str(num2%2)+bin2
            num2=num2//2  

    maxLen = max(len(bin1), len(bin2))  
    bin1 = bin1.zfill(maxLen)
    bin1 = bin1.zfill(maxLen)

    sub_bin = ''
    temp = 0
    i = maxLen - 1
    count = 0
    res = ''
    
    while(i>=0):
        sub = int(bin1[i]) - int(bin2[i])
        if sub == -1:
            if temp == 0: 
                temp = 1
                sub_bin = sub_bin + '1'
            else: 
                sub_bin = sub_bin + '0'
        elif sub == 0:
            if temp == 0: 
                sub_bin = sub_bin + '0'
                temp = 0
            else: 
                sub_bin = sub_bin + '1'
        else: 
            if temp == 0:
                sub_bin = sub_bin + '1'
            else:
                sub_bin += '0'
                temp = 0
        i -= 1   
        j = len(sub_bin) - 1
    for i in range(len(sub_bin)):
        if sub_bin[j] == '0':
            count += 1
        elif sub_bin[j] == '1':
            break
        j -= 1
    
    temp2 = sub_bin[0:-count]

    for i in range(len(temp2)-1,-1,-1):
        res += temp2[i]


    print("Num1 :", bin1)
    print("Num1 :", bin2)
    print("Sub (Binary) :", res)
    print("Sum (Decimal) :", sub_dec)


binary_substraction(60,50)
    