def highestOccurance(nums):
    count=[0]*101
    for i in nums:
        count[i]+=1

    max_freq=max(count)
    max_count=0
    for i in range(len(count)):
        if max_freq==count[i]:
            max_count=i
            break
    return max_count

nums = [1, 2, 2, 3, 3, 3]
print(highestOccurance(nums))

