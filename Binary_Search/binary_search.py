# Implement Binary Search!
import random
import time

# Define the naive approach to search first
def naive_approach(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Binary search utilizes a divide-and-counquer approach to searching a list
def binary_search(array, target, lower_index=None, higher_index=None):
    """
    Implementation of the binary search algorithm. 
    This function takes a list, a target value, and the indices of the lower half
    of the list and the higher half of the list
    """

    if lower_index is None:
        lower_index = 0
    
    if higher_index is None:
        higher_index = len(array) - 1

    if higher_index < lower_index:
        return -1

    middle_point = (lower_index + higher_index) // 2

    if array[middle_point] == target:
        return middle_point
    elif target < array[middle_point]:
        # Target is less than the middle point
        return binary_search(array, target, lower_index, middle_point-1)
    else:
        # Target is greater than the middle point
        return binary_search(array, target, middle_point + 1, higher_index)

if __name__ == '__main__':
    # Implement both functions in main
    #l = [1, 3, 5, 10, 12]
    #target = 10
    #print(naive_approach(l, target))
    #print(binary_search(l, target))

    # Timing analysis of both algorithms
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        # Give a list of random integers between -30000 - 30000
        sorted_list.add(random.randint(-3*length, 3*length))
    
    sorted_list = sorted(list(sorted_list))

    # Timing analysis for naive search
    start_time = time.time()
    for target in sorted_list:
        naive_approach(sorted_list, target)
    
    end_time = time.time()
    print("Naive search time: ", (end_time - start_time), " seconds")

    # Timing analysis for binary search
    start_time = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    
    end_time = time.time()
    print("Binary search time: ", (end_time - start_time), " seconds")

