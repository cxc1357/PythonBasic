import numpy as np

class Solution:
    def twoCitySchedCost(self,costs):
        diff = [abs(a - b) for a ,b in costs]
        # 得到倒序排列的索引，如
        # >>>np.argsort([10,30,20])[::-1]
        # array([1, 2, 0], dtype=int64)
        indices = np.argsort(diff)[::-1]
        ACount,N,minc = 0,len(costs),0
        for i, indice in enumerate(indices):
            c = costs[indice]
            # 剩余选择B
            if ACount >= N:
                minc += c[1]
            # 剩余选择A
            elif i - ACount >= N:
                minc += c[0]
            # A便宜，选择A
            elif c[0] < c[1]:
                ACount, minc = ACount + 1, minc + c[0]
            # B便宜，选择B
            else:
                ACount, minc = ACount, minc + c[1]
        return minc

if __name__ == "__main__":
    so = Solution()
    costs = [[10, 20], [50, 400], [30, 200], [30, 20]]
    res = so.twoCitySchedCost(costs)
    print(res)