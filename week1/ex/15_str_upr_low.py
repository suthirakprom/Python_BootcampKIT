string = input("Enter a string: ")
length = len(string)//2
print(f"{string.upper()[:length]}{string.lower()[length:]}")