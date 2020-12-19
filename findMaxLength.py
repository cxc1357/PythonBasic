# day50:连续数组
# 找到含有相同数量0和1的最长连续子数组
# i = 0 1 2 3 4 5
#    [0,0,0,1,1,1]
# c = 1 2 3 2 1 0
# d = {c:i}
# maxlen = max(maxlen,i-d[count])
# i=1时c=2，而当i=3时c再次=2，说明中间经过的0、1抵消
class Solution:
    def findMaxLength(self,nums):
        count,maxlen=0,0
        d = {0:-1}
        for i,num in enumerate(nums):
            if num == 0:
                count += -1
            else:
                count += 1

            if count in d:
                maxlen = max(maxlen,i-d[count])
            else:
                d[count]=i

        return maxlen

if __name__ == "__main__":
    nums = [1,0,0,0,1]
    so = Solution()
    res = so.findMaxLength(nums)
    print(res)