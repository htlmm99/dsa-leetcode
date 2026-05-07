class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_dem = 0
        dem = 0
        set_nums = set(nums)
        len_n = len(set_nums)
        for i in set_nums:
            dem = 0
            for x in range(len_n):
                if i+x in set_nums:
                    dem +=1 
                else:
                    break
            for x in range(len_n):
                if i - x - 1 in set_nums:
                    dem +=1
                else:
                    break
            if dem > max_dem:
                max_dem = dem
        return max_dem 

        