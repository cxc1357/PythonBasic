class Solution:
    def numWaterBottles(self,numBottles,numExchange):
        sumb = numBottles
        empty = numBottles
        # 只要还能换就继续
        while empty // numExchange:
            # 每轮兑换数
            bottle = empty // numExchange
            # 每轮空瓶数
            empty = bottle + empty % numExchange
            # 喝的总瓶数
            sumb += bottle
        return sumb
if __name__ == "__main__":
    so = Solution()
    res = so.numWaterBottles(9,3)
    print(res)