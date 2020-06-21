def search_in_tuple(lst, num):
    if num in lst:
        new_num = lst.index(num)
        return f"Element found at Index: {new_num}"
    else:
        return "Element not found in the tuple"


res = search_in_tuple((20,15,10,30), 10)
print(res)