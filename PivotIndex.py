def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == total - left -nums[i]:
            return i
        left += nums[i]
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))