class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        for i in range(0, len(nums)):
            nums_2 = nums[0:i] + nums[i+1:]
            # nums_2.remove(nums[i])
            re = 1
            for n in nums_2:
                re *= n
            res[i] = re
        return res 