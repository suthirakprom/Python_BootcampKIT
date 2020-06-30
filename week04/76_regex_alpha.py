import re

def regex_alpha(string): 
    if re.match("^[A-Za-z0-9_-]*$", string):
        return True
    else:
        return False

res = regex_alpha("abc123!")
print(res)