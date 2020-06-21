def slice_list(lst, num):
    return lst[slice(num, -num)]

print(slice_list([50,10,62,32,64,78,90],2))