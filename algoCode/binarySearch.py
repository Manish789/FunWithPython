# Binary Search 
# BigO Notation : O(log n), also known as log time.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while(low <= high):
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

num_list = [12,13,14,15,16,17,18,19]
print(binary_search(num_list,13))
print(binary_search(num_list,19))
print(binary_search(num_list,22))
