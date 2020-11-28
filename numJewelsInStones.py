# Day11:宝石与石头

class Solution():
    # 暴力解法，复杂度len(S)*len(J)
    def numJewelsInStones(self,J,S):
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count
    # 简单写法
    def numJewelsInStones_pythonic(self,J,S):
        return sum(s in J for s in S)
    # 使用哈希表，复杂度len(S)+len(J)
    def numJewelsInStones_hash(self,J,S):
        dict = {}
        sum = 0
        for s in S:
            dict[s] = dict.get(s,0) + 1
        for j in J:
            sum += dict.get(j,0)
        return sum

if __name__ == "__main__":
    so = Solution()
    result = so.numJewelsInStones_hash("aA","aAAbbbb")
    print(result)