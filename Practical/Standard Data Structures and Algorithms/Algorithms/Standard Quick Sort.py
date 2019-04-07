##quick sort
def quick_sort(lst):
    if lst:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1,len(lst)):
            if lst[i] > pivot:
                right.append(lst[i])
            else:
                left.append(lst[i])
    else:
        return lst
    return quick_sort(left) + [pivot] + quick_sort(right)
lst = [2,4,5,3,1,6,8,4,9,1]
print(quick_sort(lst))
