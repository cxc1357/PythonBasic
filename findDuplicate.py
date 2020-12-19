# day39 找重复数
# 数组nums包含n+1个整数，其数字在1和n之间
# 要求:
# 1.不能更改原数组
# 2.时间复杂度小于O(n2)
# 3.空间复杂度不大于O(1)
class Solution(object):
    def findDuplicate(self,nums):
        flag = 0
        for num in nums:
            if flag & (1<<num) > 0:
                return num
            else:
                flag |= (1<<num)
if __name__ == "__main__":
    nums = [1,3,2,2]
    so = Solution()
    res = so.findDuplicate(nums)
    print(res)