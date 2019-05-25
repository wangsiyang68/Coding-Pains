##sorting exercise
import random
import time

##implement bubble, insertion and quick sort
def bubble_sort(my_list):
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1],my_list[j]

    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i - 1
        this_number = my_list[i]
        while j >= 0 and this_number < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1

        my_list[j+1] = this_number

    return my_list

def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        left = []
        right = []
        pivot = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] >= pivot:
                right.append(my_list[i])
            else:
                left.append(my_list[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

def create_random_list():
    random_list = [random.randint(0,100) for i in range(1000)]
    print("\nYour random list is :",random_list)

    return random_list

##UI SCRIPT
learning = True
while learning:
    print("Lets learn about sorting")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    print("4. Quit")
    try:
        option = int(input("Please choose an option: "))

        if option == 4:
            learning = False
        else:
            original_random_list = create_random_list()
            copy_of_random_list = original_random_list[:]
            input("Press Enter to continue\n")
            if option == 1:
                start = time.time()
                for i in range(100):
                    sorted_list = bubble_sort(copy_of_random_list)
                end = time.time()
                text = "Bubble Sort returns:"
            elif option == 2:
                start = time.time()
                for i in range(100):
                    sorted_list = insertion_sort(copy_of_random_list)
                end = time.time()
                end = time.time()
                text = "Insertion Sort returns:"
            elif option == 3:
                start = time.time()
                for i in range(100):
                    sorted_list = quick_sort(copy_of_random_list)
                end = time.time()
                text = "Quick Sort returns:"
            print("Is the list sorted?", sorted_list == sorted(original_random_list))
            print("Is this implementation of the sort in place?", copy_of_random_list == sorted_list)
            print("Time taken for the sort to complete:",float(end - start)/100)
            input("Press Enter to continue\n")
        
    except:
        print("Please enter a value from 1-4")
