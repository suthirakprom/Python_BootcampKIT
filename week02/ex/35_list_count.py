def list_count(lst):
    if len(lst) < 1:
        print("Your string is empty")
    else:
        #count = 0
        uni_num = []
        num = []
        new_num = []
        # find unique number
        for i in lst:
            if i not in uni_num:
                uni_num.append(i)

        # count each element of unique number in the list
        for i in range(len(uni_num)):
            num.append(lst.count(uni_num[i]))
            # add 2 value into a list at a time
            new_num.append((uni_num[i], num[i]))

    return new_num
    
res = list_count(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"])
print(res)