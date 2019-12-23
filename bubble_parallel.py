from mpi4py import MPI
import numpy as np
import time
from operator import itemgetter

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

#Assign global variables
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    arraySize = input("Please enter array size: ")

    #Generate numbers of size n
    numbers = np.arange(int(arraySize))
    np.random.shuffle(numbers)
    print("Generated list of size " + str(arraySize) + " is: " + str(numbers))

    chunks = np.array_split(numbers, size)
else:
    chunks = None

#start script with parallel processes
start_time = time.time()

chunk = comm.scatter(chunks, root=0)
print("Process " + str(rank) +" has this chunk of data: " + str(chunk))

bubble_sort(chunk)

sortedArrays = comm.gather(chunk, root=0)

if rank == 0:
    iteratorNumbers = np.zeros((len(sortedArrays),), dtype=int)
    sortedArray = []
    for my_index in range(0, int(arraySize)):
        iterator = [ (i, (99999999 if iteratorNumbers[i] >= len(sortedArrays[i]) else sortedArrays[i][iteratorNumbers[i]]) ) for i in range(0, len(sortedArrays))]
        res = min(iterator, key = itemgetter(1))
        iteratorNumbers[res[0]] = iteratorNumbers[res[0]] + 1
        sortedArray.append(res[1])
        iterator=[]
    
    print("\n\n Sorted Array: " + str(sortedArray))

    #End of script
    print("\n\n Execution Time --- %s seconds ---" % (time.time() - start_time))
