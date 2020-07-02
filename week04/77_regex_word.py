import re

def regex_word(n, string):
    res = ""
    if n > 0: 
        splited_string = string.split()
        for i in splited_string:
            remove_char = re.sub('[a-zA-Z0-9]', ' ', i)
            a = len(i) - len(remove_char)
            if a > n: 
                res += i + " "
            elif remove_char == '': 
                pass
            else:
                res += remove_char + " "
        return res.strip()
    else: 
        return res


print(regex_word(3, "My name is Pidor"))
print(regex_word(5, "How are you today?"))
print(regex_word(2, "Is it a cat or is it a dog?"))