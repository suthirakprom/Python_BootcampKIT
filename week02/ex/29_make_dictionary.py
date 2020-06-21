def make_dictionary(lst,tp):
    dic = {}
    for i in range(len(lst)):
        dic.update({lst[i] : tp[i]})
    return dic

print(make_dictionary([50,10,62], ("Borey", "Thirak", "Dane")))