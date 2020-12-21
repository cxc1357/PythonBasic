# day 64：买卖股票最佳时间
class Solution:
    def maxProfit(self,prices):
        if not prices:
            return 0
        buyin,buyout = 10**4+1,0
        i,c,sump = 0,len(prices),0
        while i < c:
            # 找第一个低点
            while i < c and prices[i] < buyin:
                buyin = prices[i]
                i += 1
            # 找第一个高点
            while i < c and buyout < prices[i]:
                buyout = prices[i]
                i += 1
            # 一次收益
            sump += max(0,buyout - buyin)
            buyin,buyout = 10**4+1,0
        return sump
if __name__ == "__main__":
    so = Solution()
    prices = [7,1,5,3,6,4]
    res = so.maxProfit(prices)
    print(res)        