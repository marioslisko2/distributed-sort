def merge_sort(list):
    list_length = len(list)
    
    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)

def merge(left, right):
   
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
       
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    output.extend(left[i:])
    output.extend(right[j:])

    return output
#########
import numpy as np
import math

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

root = 0

max_processors = comm.size
data = [3,5,7,4,6,7,11,9,2,8,3,2]
new_list = []
# Bin size
bin_size = math.floor(int((max(data)-min(data))/comm.size))
# Store appropriate numbers in their bins
for rank in range(max_processors):
    new_list.append([x for x in data if (x >= bin_size*rank+rank) and x<=(bin_size+bin_size*rank+rank)])
# Scatter the lists among the max # of processors
v = comm.scatter(new_list,root)
print("Rank:",comm.rank, " ", v)
# Sort each of the lists that each processor gets
mrgSort = merge_sort(v)
# Gather all the sorted lists
g = comm.gather(mrgSort,root)
print("-------------------------")
if comm.rank==0:
    for i in range(len(g)):
        print("Rank:",i," ",g[i])
    print(g)

