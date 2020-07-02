import re

def regex_par(n, string): 
    s = ""
    s += re.sub(r"(.*?)\s?\(.*?\)", r"\1", string).lower()
    print(s)

regex_par("hello (it) (( i (w)ase me")