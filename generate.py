# day24:生成杨辉三角的前n行
class Solution():
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            yanghui = self.generate(numRows -1)
        last_row = [1] + [yanghui[-1][i-1] + yanghui[-1][i] for i in range(1,numRows -1)] + [1]
        yanghui.append(last_row)
        return yanghui

if __name__ == "__main__":
    so = Solution()
    result = so.generate(4)
    print(result)
