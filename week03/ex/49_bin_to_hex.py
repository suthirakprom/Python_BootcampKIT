def bin_to_hex(input_bin):
    bin_num = input_bin
    bin_arr = ['0000','0001', '0010', '0011', '0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    count = 0
    for i in range(len(bin_num)):
        if bin_num[i] != '0' and bin_num[i] != '1':
            count += 1
    if count == 0:

        # adding enough digit to make 
        while(len(bin_num)%4 != 0):
            bin_num = '0' + bin_num
            #print(bin_num)

        # split binary by 4 
        splited_bin = [bin_num[i:i+4] for i in range(0, len(bin_num), 4)]
        # print(splited_bin)
        res = ''
        for i in range(len(splited_bin)):
            index_from_bin = bin_arr.index(splited_bin[i])
            if index_from_bin == 10: 
                res += 'A'
            elif index_from_bin == 11:
                res += 'B'
            elif index_from_bin == 12:
                res += 'C'
            elif index_from_bin == 13:
                res += 'D'
            elif index_from_bin == 14:
                res += 'E'
            elif index_from_bin == 15:
                res += 'F'
            else:
                res += str(bin_arr.index(splited_bin[i]))
        print(res)

    else:
        print('This is not a binary number')
        
bin_to_hex('11001101')
    
    