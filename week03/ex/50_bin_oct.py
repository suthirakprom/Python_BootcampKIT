def bin_oct(input_bin):
    bin_num = input_bin
    bin_arr = ['000','001','010','011','100','101','110','111']
    count = 0
    for i in range(len(bin_num)):
        if bin_num[i] != '0' and bin_num[i] != '1':
            count += 1
   
    if count > 0 :
        print('This is not a binary number')
    else: 

        # adding 0 if it is not enough digit in the binary num
        while(len(bin_num)%3 != 0):
            bin_num = '0' + bin_num
        
        splited_bin = [bin_num[i:i+3] for i in range(0, len(bin_num), 3)]
        res = ''
        for i in range(len(splited_bin)):
            res += str(bin_arr.index(splited_bin[i]))
        print(res)

bin_oct('11001101')