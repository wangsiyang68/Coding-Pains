## Searching

There are 3 main types of searches to know, and they can be classified according to their time complexities. 

According to the situations, you are usually asked to write a function that takes in an item (that you want to search), a list (to search for item) and returns the (1) index or (2) a boolean value that tells you if the item is present

| Worst Case  | O(n)                                            | O(nlgn)                                                      | O(1)                                                        |
| ----------- | ----------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| Search Name | Linear Search                                   | Binary Search                                                | Hash Table Search                                           |
| Description | Search for an item in a list from left to right | Search for an item in a sorted list by repeatedly shifting upper and lower bounds | Search for an item in a Hashtable using a unique hash value |

**Pseudocode**

Here are the pseudocode implementations of the 3 searches:

<u>Linear Search</u>

```def linear_search(item, array)
NotFound = True
index = 0
while NotFound and index < len(array):
if array[index] == item:
	NotFound = False
return NotFound (or return index if need be)
```

**Analysis:** This search has a worst case scenario when the item is last in the array/ not found in the array

<u>Binary Search</u>

```def binary_search(item, array)
lower_bound = 0
upper_bound = len(array)
NotFound = True
while lower_bound <= upper_bound and NotFound: #important to allow possibility of lower bound = upper bound
	pointer = (lower_bound + upper_bound) // 2
	if array[pointer] == item:
		NotFound = False
	elif array[pointer] > item:
		upper_bound = pointer - 1 #important to exclude pointer
	else:
		lower_bound = pointer + 1 #as above
return NotFound (or pointer if need to return index)
```

**Analysis:** Do note that this function relies on the premise that the list is sorted. If not, it would be illogical to assume an upper and lower bound in the list. The worse case scenario is the item being found at the extreme ends of the list/not found at all, which results in the while loop being run log2n times.

<u>Hash Table Search</u>

Before we read the pseudocode for Hash Table Search, we need to first define some of the concepts that are used in Hash Table Search

1. Weighted Modulo
2. Collisions
3. Methods to overcome collisions:
   1. Bucket Chaining
   2. Linear Probing

_Weighted Modulo_

Weighted Modulo is simply the number in each node of the array multiplied by its index. For example:

9920876 would have a hash value of 9 * 0 + 9 * 1 + 2 * 2 + 0 * 3 + 8 * 4 + 7 * 5 + 6 * 6 = 9 + 4 + 32 + 35 + 36 = 
