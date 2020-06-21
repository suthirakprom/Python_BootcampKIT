def dict_values(dic):
    n = len(dic)
    for i in dic:
        value = dic.get(i)
        new_string = ''
        for j in range(len(value)):
            new_string += value[j] + " "
        print(f"{i} : {new_string}")
        if n > 1:
            print("*"*5)
            n -= 1

dict_values({120: ("Visal", "Borey", "Sovann"), 130: ("Hout", "Mouyleng", "Pidor"), 140: ("Nary", "Misora", "Masaaki")})