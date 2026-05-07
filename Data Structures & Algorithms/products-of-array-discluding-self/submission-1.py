class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        index0 = []
        s = 1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                index0.append(i)
            else:
                s *= nums[i]
        if len(index0) == 0:
            res = [1] * len(nums)
            for i in range(0, len(nums)):
                res[i] = int(s/ nums[i])
            return res
        res = [0]*len(nums)
        if len(index0) > 1: 
            return res
        res[index0[0]] = s
        return res