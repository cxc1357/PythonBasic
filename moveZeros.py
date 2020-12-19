# day37:把零移到末尾
class Solution(object):
    def moveZeros(self,nums):
        fast, slow=0,0
        while fast<len(nums):
            if nums[fast] != 0:
                if fast > slow:
                    nums[slow], nums[fast] = nums[fast],0
                slow += 1
            fast += 1
        return nums

if __name__=="__main__":
    nums = [0,1,0,3,12]
    so = Solution()
    result = so.moveZeros(nums)
    print(result)
