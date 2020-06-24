def binary_addtion(num1, num2):
    sum_dec = num1 + num2
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

    #do the sum of binary
    maxLen = max(len(bin1), len(bin2))  
    bin1 = bin1.zfill(maxLen)
    bin1 = bin1.zfill(maxLen)

    sum_bin = ''
    temp = 0
    
    for i in range(maxLen-1,-1,-1):
        temp2 = temp
        if bin1[i] == '1':
            temp2 += 1
        else: 
            temp2 += 0
        if bin2[i] == '1': 
            temp2 += 1
        else: 
            temp2 += 0

        sum_bin = ('1' if temp2%2==1 else '0') + sum_bin
        temp = 0 if temp2<2 else 1
    
    if temp != 0: 
        sum_bin = '1' + sum_bin
    #end    


    print("Num1 :", bin1)
    print("Num1 :", bin2)
    print("Sum (Binary) :", sum_bin)
    print("Sum (Decimal) :", sum_dec)


binary_addtion(60,50)
    