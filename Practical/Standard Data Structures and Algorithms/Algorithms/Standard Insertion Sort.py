##insertion sort
def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i - 1
        current = lst[i]
        while current < lst[j] and j >= 0:
            lst[i] = lst[j]
            j -= 1
            i -= 1
        lst[i] = current
    return lst

lst = [2,4,5,3,1,6,8,4,9,1]
print(insertion_sort(lst))
