##total time taken: 1h11min
##bubble sort 1047

a = [5,35,1,3,42,5,4,473,863,63,30,99]

def b_sort(lst):
    for i in range(0,len(lst)):
        for j in range(i,len(lst)-1):
            if lst[j-i] > lst[j-i+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
    return lst

print(b_sort(a))

##insertion sort 1055
def i_sort(lst):
    for i in range(0,len(lst)-1):
        j = i + 1
        if lst[j] < lst[i]:
            while i > 0:
                if lst[j] < lst[i-1]:
                    i -= 1
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = lst[i]

    return lst
    
print(i_sort(a))


##merge sort 1103

def m_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        return m_list(m_sort(lst[:len(lst)//2]),m_sort(lst[len(lst)//2:]))
    
def m_list(lst1,lst2):
    i = 0
    j = 0
    result = []
    while lst1 and lst2:
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            lst1 = lst1[1:]
        else:
            result.append(lst2[j])
            lst2 = lst2[1:]
    return result + lst1 + lst2

print(m_sort(a))

##quick sort 1111

def q_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1,len(lst)):
            if lst[i] > pivot:
                right.append(lst[i])
            else:
                left.append(lst[i])

    return q_sort(left) + [pivot] + q_sort(right)

print(q_sort(a))

