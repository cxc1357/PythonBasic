#day55：一维数组动态和

class Solution:
    def runningSUm(self,nums):
        if not nums:
            return []
        
        # 预先申请空间，放置扩容时的时间消耗
        r,s = [0]*len(nums),0
        for i,num in enumerate(nums):
            s += num
            r[i] = s
        return r

if __name__ == "__main__":
    so = Solution()
    res = so.runningSUm([1,2,3])
    print(res)
