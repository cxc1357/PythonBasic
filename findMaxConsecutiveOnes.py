#day38最大连续1个数
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi,count = 0,0
        for num in nums:
            if num == 0:
                maxi = max(maxi,count)
                count = 0
            else:
                maxi = max(maxi,count + 1)
                count += 1
        return maxi

if __name__ == "__main__":
    nums = [1,1,0,1,1,1,1]
    so = Solution()
    result = so.findMaxConsecutiveOnes(nums)
    print(result)
