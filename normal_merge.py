def merge_sort(list): #merge sort je objasnjen u distribuited_merge.py datoteci
    list_length = len(list)
    
    if list_length==1:
        return list

    mid_point = list_length//2

    left_partition=merge_sort(list[:mid_point])
    right_partition=merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1
    
    output.extend(left[i:])
    output.extend(right[j:])

    return output

data = []

with open("Random.txt") as file:
    while line:=file.readline().rstrip():
        data.append(int(line))

file.close()
mrgSort=merge_sort(data)
#print(mrgSort)
