# day42:切分可排序数组

class Solution(object):
    # 常规解法
    # python内置max, min均为O(n)复杂度
    def maxChunksToSorted(self,arr):
        count = 0
        for i in range(1,len(arr)):
            p1 = arr[:i]
            p2 = arr[i:]
            if max(p1) <= min(p2):
                count += 1
        return count + 1

    # 假设arr是[0,1,...,arr.length-1]的一种排列
    # 若索引i等于[0,i]最大值，则可分割
    def maxChunksToSorted_quick(self,arr):
        maxn,count = arr[0],0
        for i,num in enumerate(arr):
            maxn = max(maxn, num)
            if i == maxn:
                count += 1
        return count

if __name__ == "__main__":
    so = Solution()
    nums = [4,0,1,2,3]
    result = so.maxChunksToSorted_quick(nums)
    print(result)