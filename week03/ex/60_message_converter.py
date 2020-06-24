def message_converter(msg):
    ascii_value = ''
    for i in range(len(msg)):
        ascii_value = ord(msg[i])
        arrHex = [0] * 20
        n = 0
        while(ascii_value!=0):
            r = ascii_value % 16
            ascii_value = ascii_value //16
            if r < 10:
                arrHex[n] = r
                n += 1
            else: 
                arrHex[n] = chr(r+55)
                n += 1
        for i in range(n-1, -1, -1):
            print(arrHex[i], end='')

message_converter("Hello")
