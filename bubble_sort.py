import numpy as np
import time

#Bubble sort algorithm
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]


#User input size
arraySize = input("Please enter array size: ")

#Generate numbers of size n
numbers = np.arange(int(arraySize))
np.random.shuffle(numbers)
print("Generated list of size " + str(arraySize) + " is:" + str(numbers))

#start script with parallel processes
start_time = time.time()

bubble_sort(numbers)
print("\n\n Sorted Array: " + str(numbers))

#End of script
print("\n\n Execution Time --- %s seconds ---" % (time.time() - start_time))