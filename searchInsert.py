#day34 寻找有序数组元素插入位置

class Solution(object):
    def searchInsert(self,nums,target):
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        return left
if __name__ == "__main__":
    nums = [1,3,3,5]
    target = 4
    so = Solution()
    result = so.searchInsert(nums,target)        
    print(result)