##bubble sort

lst = [4,13,5,8,4,5,2,7,8,8,45,22]
def bubble_sort(lst):
    for i in range(len(lst)): #number of times that we need to do this
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

print('bubble sort returns', bubble_sort(lst))


lst = [4,13,5,8,4,5,2,7,8,8,45,22]
def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i-1
        number = lst[i]
        while number < lst[j] and j>=0 :
            lst[i] = lst[j]
            j -= 1
            i -= 1
        lst[i] = number
                
    return lst

print('insertion sort returns', insertion_sort(lst))

lst = [4,13,5,8,4,5,2,7,8,8,45,22]
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        return merge_lists(merge_sort(lst[0:len(lst)//2]),merge_sort(lst[len(lst)//2:]))

def merge_lists(lst1,lst2):
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1[0])
            lst1 = lst1[1:]
        else:
            result.append(lst2[0])
            lst2 = lst2[1:]
    return result + lst1 + lst2

print('merge sort returns', merge_sort(lst))

lst = [4,13,5,8,4,5,2,7,8,8,45,22]
def quick_sort(lst):
    if lst:
        left = []
        right = []
        pivot = lst[0]
        for i in range(1,len(lst)):
            if lst[i] > pivot:
                right.append(lst[i])
            else:
                left.append(lst[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return lst

print('quick sort returns', quick_sort(lst))
