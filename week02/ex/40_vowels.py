def vowels(string):
    count = 0
    splitStr = string.split()
    new_str = ''
    vowel = ('a', 'e', 'i', 'o', 'u')
    for i in string.lower():
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'i':
            count += 1
            new_str += i
        if i == ' ':
            string = string.replace(i, '')
        if i in vowel:
            string = string.replace(i, '')
    if count == 0:
        print("NO VOWELS")
    else:
        print(count)
        print(new_str)
        print(string.upper())
    

vowels("What is that?")