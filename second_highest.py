def second_highest(arr):
    count=[0]*101
    for i in arr:
        count[i]+=1

    max_freq=max(count)
    second_max=0
    for i in range(len(count)):
        if count[i]<max_freq and count[i]>second_max:
            second_max=i

    if second_max==0:
        return -1

    for i in range(len(count)):
        if count[i]==second_max:
            return i

    return second_max

nums = [1, 2, 2, 3, 3, 3]
print(second_highest(nums))