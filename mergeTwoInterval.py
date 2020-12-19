# day36：合并区间
class Solution:
    def merge(self,intervals):
        ret = []
        if len(intervals) == 0:
            return ret
        # 按区间起始元素排序
        intervals = sorted(intervals)
        # 当前区间端点
        l,r = intervals[0]
        # 遍历区间列表，进行合并
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            # 如果可以合并，维护合并后的右端点
            if s <= r:
                r = max(r,e)
            else:
            # 否则加入答案，将i作为当前进行合并的区间
                ret.append([l,r])
                l,r = s,e
        ret.append([l,r])
        return ret

if __name__ == "__main__":
    input = [[1,3],[2,6],[8,10],[15,18]]
    so = Solution()
    result = so.merge(input)
    print(result)