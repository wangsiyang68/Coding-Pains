lst = ['a','b','c','d','e','f','g','h','i','j']
print('iterative version')
##iterative version
for item in lst:
    low = 0
    high = len(lst)-1
    while low <= high:
        index = (low + high)//2
        if lst[index] == item:
            print(lst[index])
            break
        else:
            if item <= lst[index]:
                high = index-1
            else:
                low = index + 1

    if low > high:
        print('Sorry')
        
print('recursive version')
##recursive version
def search(item,lst = lst):
    index = len(lst)//2

    if lst == []:
        return None
    if lst[index][0] == item:
        return lst[index]
    else:
        if item < lst[index]:
            return search(item,lst[:index])
        else:
            return search(item,lst[index+1:])

for i in lst:
    print(search(i))
