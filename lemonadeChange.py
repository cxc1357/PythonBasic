# day65：柠檬水找零
class Solution:
    def lemonadeChange(self,bills):
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if ten < 0 or five < 0:
                return False
        return True
if __name__ == "__main__":
    so = Solution()
    bills = [5,5,5,10,10,20]
    res = so.lemonadeChange(bills)
    print(res)
