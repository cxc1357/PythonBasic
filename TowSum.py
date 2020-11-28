class Solution:
    def TwoSum(self,nums,target):
        dict={}
        # enumerate例子：
        # >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        # >>> list(enumerate(seasons))
        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        # 遍历的同时把列表的值存在字典中
        for i,n in enumerate(nums):
            if target-n in dict:
                return [dict[target-n],i]
            else:
                dict[n] = i

if __name__ == "__main__":
    so = Solution()
    # 输入：[1,8,9,2,6],10
    # 输出：[0,2]
    result = so.TwoSum([1,8,9,2,6],10)
    print(result)