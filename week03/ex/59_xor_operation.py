def xor_operation(h1,h2):
    n1 = int(h1,16)
    res = ''
    bin_num1 = ''
    count = 0
    while n1>0: 
        bin_num1 = str(n1%2) + bin_num1
        n1 = n1 // 2
    n2 = int(h2,16)
    bin_num2 = ''
    while n2>0: 
        bin_num2 = str(n2%2) + bin_num2
        n2 = n2 // 2
    maxLen = max(len(bin_num1),len(bin_num2))
    bin_num1 = bin_num1.zfill(maxLen)
    bin_num2 = bin_num2.zfill(maxLen)
    for i in range(maxLen):
        if bin_num1[i] != bin_num2[i]:
            res += '1'
        else:
            res += '0'
    for i in range(len(res)):
        if res[i] == '0':
            count += 1
        elif res[i] == '1':
            break

    print(bin_num1)
    print(bin_num2)
    print('')
    print(res[count:])
xor_operation("33", "3D")