def firstDuplicate(nums: list[int]) -> int:
    count={}
    for i in nums:
        if i in count:
            return i
        else:
            count[i]=1

    return -1

print(firstDuplicate([2, 1, 3, 5, 3, 2]))