class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic[x] + 1 if x in dic else 0
        ls = sorted(list(dic.values()))
        flag_num = ls[-k]

        result = []
        for x, count in dic.items():
            if count >= flag_num:
                result.append(x)
        return result