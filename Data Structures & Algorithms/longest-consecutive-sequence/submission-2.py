class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_dem = 0
        set_nums = set(nums)
        for x in set_nums:
            if x -1 not in set_nums:
                length = 1
                while (x + length) in set_nums:
                    length+=1
                if length > max_dem:
                    max_dem = length
        return max_dem


        