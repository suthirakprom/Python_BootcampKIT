def list_merge_sort(lst):
    if len(lst)>1: 
        mid = len(lst)//2
        leftHaft = lst[:mid]
        rightHaft = lst[mid:]

        list_merge_sort(leftHaft)
        list_merge_sort(rightHaft)
        i=j=k=0
        while i < len(leftHaft) and j < len(rightHaft):
            if leftHaft[i] < rightHaft[j]:
                lst[k] = leftHaft[i]
                i += 1
            else:
                lst[k] = rightHaft[j]
                j += 1
            k += 1

        while i < len(leftHaft): 
            lst[k] = leftHaft[i]
            i += 1
            k += 1
        while j < len(rightHaft):
            lst[k] = rightHaft[j]
            j += 1
            k += 1
    return lst

res = list_merge_sort([50, 75, 60, 55, 60, 98, 23])
rev_list = []
for i in range(len(res)-1, 0, -1):
    rev_list.append(res[i])
print(rev_list)