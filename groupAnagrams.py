# Day10：异位词分组（哈希表键的设计）
class Solution:
    def groupAnagrams(self,strs):
        dict={}
        for s in strs:
            # 将字符串排序后的元组作为哈希表的键
            # >>> sorted("bca")
            # ['a', 'b', 'c']
            # >>> tuple(sorted("bca"))
            # ('a', 'b', 'c')
            key = tuple(sorted(s))
            # 返回指定键的值，若不存在返回默认值[]
            dict[key] = dict.get(key,[]) + [s]
        return list(dict.values())

if __name__ == "__main__":
    so = Solution()
    result = so.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    # 输出：[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(result)
