# day31 递归快速幂算法
# 求x的n次幂，一般解算法时间复杂度为O(n)，递归解法为O(logn)
class Solution:
    def myPow(self, x,n):
        # 基情况
        if n == 0:
            return 1
        # 负数次幂的情况
        if n < 0:
            x,n = 1/x, -n
        # 递归减半,x^(2n)=x^(n)^2    
        t = n//2
        p = self.myPow(x,t)
        # 按n的奇偶讨论返回值p
        return p**2*x if n&1 else p**2

if __name__ == "__main__":
    so = Solution()
    result = so.myPow(2,7)
    print(result)