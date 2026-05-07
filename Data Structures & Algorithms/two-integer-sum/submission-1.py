class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            dic[nums[i]] = i
        for i in range(n):
            x = target - nums[i]
            if x in dic:
                if i == dic[x]: 
                    continue
                return [i, dic[x]]