def sumofhighandlow(arr):
    count=[0]*101
    for i in arr:
        count[i]+=1

    max_freq=max(count)
    highest_freq=max_freq
    lowest=0

    for i in range(len(count)):
        if count[i]>0:
            if lowest==0 or count[i]<lowest:
                lowest=count[i]
    return highest_freq+lowest

nums = [1, 2, 2, 3, 3, 3]
print(sumofhighandlow(nums))