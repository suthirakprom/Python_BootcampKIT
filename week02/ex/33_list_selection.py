def list_selection(lst):
    for i in range(len(lst)-1, 0, -1):
        n = 0
        for j in range(1, i+1):
            if lst[j]>lst[n]:
                n = j
        temp = lst[i]
        lst[i] = lst[n]
        lst[n] = temp
    return lst

res = list_selection([50,75,60,55,98,28])
print(res)