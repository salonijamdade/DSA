def least_count(arr):
    count=[0]*100
    for i in range(len(arr)):
        count[arr[i]]+=1

    least_occuring=float('inf')

    for i in range(len(count)):
        if count[i]< least_occuring and count[i]>0:
            least_occuring=count[i]

    for i in range(len(count)):
        if count[i] == least_occuring:
            return i

    return -1

count=[1,2,1,1,1,1,3,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,7,7,7,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
print(least_count(count))