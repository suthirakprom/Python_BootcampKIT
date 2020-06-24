

def hex_to_oct(hex_num): 
    num_arr = ['0','1','2','3','4','5','6','7','8','9']
    hex_num = hex_num.upper()
    count = 0
    for i in hex_num: 
        if i > 'F':
            count += 1
        
    if count > 0:
        print("This is not a hexa-decimal number")
    else:
        oct = ""
        i,dec = 0, 0
        j = len(hex_num)-1
        while i < len(hex_num):
            n = hex_num[i]
            if n in num_arr:
                dec += int(n) * int(16**j)
            elif n == 'A':
                dec += 10 * int(16**j)
            elif n == 'B':
                dec += 11 * int(16**j)
            elif n == 'C':
                dec += 12 * int(16**j)
            elif n == 'D':
                dec += 13 * int(16**j)
            elif n == 'E':
                dec += 14 * int(16**j)
            elif n == 'F':
                dec += 15 * int(16**j)

            i += 1
            j -= 1

        while(dec):
            oct = "".join([str(int(dec % 8)), oct])
            dec = dec//8
        
        print(oct)

hex_to_oct("2b9")