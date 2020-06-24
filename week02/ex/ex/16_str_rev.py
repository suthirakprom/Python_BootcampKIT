string = input("Input a string:")
length = len(string)//2
string2 = string[:length][::-1]
print(f"{string2}{string[length:]}")