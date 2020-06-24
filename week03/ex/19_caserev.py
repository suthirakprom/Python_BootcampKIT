string = input("Enter a string: ")
string2 = ''
if string == '':
    print("Empty")
else:  
    for i in range(0, len(string)):  
            ascii = ord(string[i])   
            if ascii >= ord('a') and ascii <= ord('z'):  
    
                string2 += chr(ascii - 32) 
                
            elif ascii >= ord('A') and ascii <= ord('Z'): 
                string2 += chr(ascii + 32) 
    
print(string2)  
