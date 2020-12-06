# day25:递归计算斐波那契数列第n项，使用记忆搜索法消除重复计算
from functools import lru_cache

class Solution():
    memo = {}
    def fib(self, N):
        if N < 2:
            return N
        if N-1 not in self.memo:
            self.memo[N-1] = self.fib(N-1)
        if N-2 not in self.memo:
            self.memo[N-2] = self.fib(N-2)
        return self.memo[N-1] + self.memo[N-2]
    
    # lru_cache是python的缓存库，采用注解方式使用
    @lru_cache()
    def fib_lru(self,N):
        if N < 2:
            return N
        return self.fib_lru(N-1) + self.fib_lru(N-2)

if __name__ == "__main__":
    so = Solution()
    result = so.fib_lru(6)
    print(result)
