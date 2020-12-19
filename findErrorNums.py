# day43：找到重复值
# 无序数组S包含1到n的整数，其中有一个元素是重复的
# input：nums=[1,2,2,4]
# output: [2,3]
# 利用索引key=nums[i] - 1 
class Solution(object):
    def findErrorNums(self,nums):
        r = [0,0]
        for i,num in enumerate(nums):
            key = abs(num) - 1
            val = nums[key]
            # 标记重复元素的位置
            if val < 0:
                r[0] = key + 1
            # 访问过的元素乘以-1
            else:
                nums[key] = -val
        
        # 重复值大于0，不会被遍历到        
        for i,num in enumerate(nums):
            if num > 0:
                r[1] = i + 1
        return r
    

