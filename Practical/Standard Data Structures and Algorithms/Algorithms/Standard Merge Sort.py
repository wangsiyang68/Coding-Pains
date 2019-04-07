##merge sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    return merge_lists(merge_sort(lst[:len(lst)//2]),merge_sort(lst[len(lst)//2:]))

def merge_lists(lst1,lst2):
    array = []
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            array.append(lst1[0])
            lst1 = lst1[1:]
        else:
            array.append(lst2[0])
            lst2 = lst2[1:]
    return array + lst1 + lst2

lst = [2,4,5,3,1,6,8,4,9,1]
print(merge_sort(lst))
