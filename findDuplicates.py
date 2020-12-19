# day44:数组可能取值范围[1,n],判断是否存在重复元素
# 每次将key = abs(nums)-1 标记为负值，若访问到负值，则说明有重复元素
def findDuplicates(nums):
    for num in nums:
        key = abs(num) - 1
        if nums[key] < 0:
            return True
        else:
            nums[key] *= -1
    return False

print(findDuplicates([1,3,1,1]))

