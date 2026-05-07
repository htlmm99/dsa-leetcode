class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        pre_s = [0] * n
        suf_s = [0] * n
        pre_s[0] = 1
        suf_s[n-1] = 1
        for i in range(1, n):
            pre_s[i] = pre_s[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suf_s[i] = suf_s[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pre_s[i] * suf_s[i]
        return res 