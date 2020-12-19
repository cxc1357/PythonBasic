# day51:连续最长子串
# 条件：每个元音字母都恰好出现偶数次
# 0 1 2 4 8 16
# - a e i o u
# 编码元音字母，使其在二进制表示下都只有一位为1
# 对新字母进行异或运算后，若某个元音出现偶数次，则对应位最终状态必为0
# statedict记录{状态：位置}
class Solution:
    def findTheLongestSubstring(self,s):
        state,statedict = 0,{0:-1}
        maxlen = 0
        codedict = {'a':1,'e':2,'i':4,'o':8,'u':16}
        for i,c in enumerate(s):
            # 异或运算记录状态
            if c in codedict:
               state ^= codedict[c]
            if state in statedict:
                maxlen = max(maxlen, i - statedict[state])
            else:
                statedict[state] = i
        return maxlen

if __name__ == "__main__":
    so = Solution()
    res = so.findTheLongestSubstring("leetcode")
    print(res)