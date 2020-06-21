def list_unique(lst):
    unique_num = []
    for i in lst: 
        if i not in unique_num:
            unique_num.append(i)
    print(unique_num)

list_unique([50,60,25,65,25,60])